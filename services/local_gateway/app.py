from __future__ import annotations

from fastapi import FastAPI
from fastapi.responses import StreamingResponse

from packages.contracts import APP_NAME, APP_VERSION, OperationEvent, OperationRequest, RobotOperation
from services.local_gateway.capabilities import get_fake_capability_inventory
from services.local_gateway.events import EventStore
from services.local_gateway.operations import FakeOperationRunner
from services.local_gateway.safety import SafetyGate


def create_app() -> FastAPI:
    events = EventStore()
    safety_gate = SafetyGate()
    runner = FakeOperationRunner(safety_gate=safety_gate, events=events)
    app = FastAPI(title="Hashtag Robotic Studio Local Gateway", version=APP_VERSION)
    app.state.events = events
    app.state.safety_gate = safety_gate
    app.state.runner = runner

    @app.get("/health")
    def health() -> dict:
        return {
            "app": APP_NAME,
            "version": APP_VERSION,
            "status": "ok",
            "mode": "local_fake",
            "physical_motion_enabled": False,
        }

    @app.get("/capabilities")
    def capabilities() -> dict:
        return get_fake_capability_inventory().model_dump(mode="json")

    @app.get("/events")
    def event_stream(limit: int = 50) -> StreamingResponse:
        if not events.list(limit=1):
            events.append(
                OperationEvent(
                    source="local_gateway",
                    type="event_stream_opened",
                    payload={"physical_motion_enabled": False},
                )
            )
        return StreamingResponse(events.as_sse(limit=limit), media_type="text/event-stream")

    @app.post("/operations/fake")
    def run_fake_operation(request: OperationRequest) -> dict:
        operation = RobotOperation.from_request(request)
        operation, safety = runner.run(operation)
        return {
            "operation": operation.model_dump(mode="json"),
            "safety": safety.model_dump(mode="json"),
            "events": [event.model_dump(mode="json") for event in events.list(limit=20) if event.operation_id == operation.id],
        }

    return app


app = create_app()
