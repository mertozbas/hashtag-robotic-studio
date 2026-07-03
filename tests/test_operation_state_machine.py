import pytest

from packages.contracts import OperationRequest, OperationStatus, RobotOperation
from services.local_gateway.events import EventStore
from services.local_gateway.operations import FakeOperationRunner, InvalidTransition, OperationStateMachine
from services.local_gateway.safety import SafetyGate


def test_fake_operation_completes_without_physical_motion() -> None:
    events = EventStore()
    operation = RobotOperation.from_request(OperationRequest(type="fake_diagnostic"))

    operation, result = FakeOperationRunner(SafetyGate(), events).run(operation)

    assert result.allowed is True
    assert operation.status == OperationStatus.COMPLETED
    assert [event.type for event in events.list()] == [
        "operation_pending_preflight",
        "preflight_allowed",
        "operation_ready",
        "operation_running",
        "operation_completed",
    ]
    assert events.list()[-1].payload["physical_motion"] is False


def test_invalid_transition_is_rejected() -> None:
    machine = OperationStateMachine(RobotOperation.from_request(OperationRequest()), EventStore())

    with pytest.raises(InvalidTransition):
        machine.transition(OperationStatus.RUNNING, "operation_running")
