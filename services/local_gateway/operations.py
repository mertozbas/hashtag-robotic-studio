from __future__ import annotations

from packages.contracts import OperationEvent, OperationStatus, RobotOperation, SafetyGateResult
from services.local_gateway.events import EventStore
from services.local_gateway.safety import SafetyGate


ALLOWED_TRANSITIONS: dict[OperationStatus, set[OperationStatus]] = {
    OperationStatus.DRAFT: {OperationStatus.PENDING_PREFLIGHT, OperationStatus.ABORTED},
    OperationStatus.PENDING_PREFLIGHT: {
        OperationStatus.BLOCKED,
        OperationStatus.AWAITING_USER_UNLOCK,
        OperationStatus.READY,
        OperationStatus.FAILED,
    },
    OperationStatus.BLOCKED: {OperationStatus.PENDING_PREFLIGHT, OperationStatus.ABORTED},
    OperationStatus.AWAITING_USER_UNLOCK: {OperationStatus.READY, OperationStatus.BLOCKED, OperationStatus.ABORTED},
    OperationStatus.READY: {OperationStatus.RUNNING, OperationStatus.ABORTED},
    OperationStatus.RUNNING: {OperationStatus.STOPPING, OperationStatus.COMPLETED, OperationStatus.FAILED},
    OperationStatus.STOPPING: {OperationStatus.COMPLETED, OperationStatus.ABORTED, OperationStatus.FAILED},
    OperationStatus.COMPLETED: set(),
    OperationStatus.FAILED: set(),
    OperationStatus.ABORTED: set(),
}


class InvalidTransition(ValueError):
    pass


class OperationStateMachine:
    def __init__(self, operation: RobotOperation, events: EventStore) -> None:
        self.operation = operation
        self.events = events

    def transition(self, status: OperationStatus, event_type: str, payload: dict | None = None) -> OperationEvent:
        allowed = ALLOWED_TRANSITIONS[self.operation.status]
        if status not in allowed:
            raise InvalidTransition(f"{self.operation.status.value} -> {status.value} is not allowed")
        previous = self.operation.status
        self.operation.status = status
        event = OperationEvent(
            operation_id=self.operation.id,
            source="operation_state_machine",
            type=event_type,
            payload={"from": previous.value, "to": status.value, **(payload or {})},
        )
        return self.events.append(event)


class FakeOperationRunner:
    def __init__(self, safety_gate: SafetyGate, events: EventStore) -> None:
        self.safety_gate = safety_gate
        self.events = events

    def run(self, operation: RobotOperation) -> tuple[RobotOperation, SafetyGateResult]:
        machine = OperationStateMachine(operation, self.events)
        machine.transition(OperationStatus.PENDING_PREFLIGHT, "operation_pending_preflight")
        result = self.safety_gate.evaluate(operation)
        self.events.append(
            OperationEvent(
                operation_id=operation.id,
                source="safety_gate",
                type="preflight_allowed" if result.allowed else "preflight_blocked",
                payload=result.model_dump(mode="json"),
            )
        )

        if not result.allowed:
            machine.transition(OperationStatus.BLOCKED, "operation_blocked", {"blockers": result.blockers})
            return operation, result

        machine.transition(OperationStatus.READY, "operation_ready")
        machine.transition(OperationStatus.RUNNING, "operation_running", {"adapter": "fake"})
        machine.transition(OperationStatus.COMPLETED, "operation_completed", {"physical_motion": False})
        return operation, result
