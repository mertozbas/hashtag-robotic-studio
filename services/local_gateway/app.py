from __future__ import annotations

from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.staticfiles import StaticFiles

from packages.contracts import APP_NAME, APP_VERSION, OperationEvent, OperationRequest, RobotOperation, SafetyLevel, SecretUpdateRequest
from services.local_gateway.capabilities import get_fake_capability_inventory
from services.local_gateway.events import EventStore
from services.local_gateway.inventory import get_read_only_inventory
from services.local_gateway.operations import FakeOperationRunner
from services.local_gateway.safety import SafetyGate
from services.local_gateway.studio import (
    get_operation_templates,
    get_packaging_plan,
    get_policy_compatibility,
    list_api_key_providers,
    list_agent_tools,
    list_dataset_summaries,
)


def create_app() -> FastAPI:
    events = EventStore()
    safety_gate = SafetyGate()
    runner = FakeOperationRunner(safety_gate=safety_gate, events=events)
    app = FastAPI(title="Hashtag Robotic Studio Local Gateway", version=APP_VERSION)
    app.state.events = events
    app.state.safety_gate = safety_gate
    app.state.runner = runner
    app.state.secret_last_four = {}
    app.state.secret_values = {}

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

    @app.get("/inventory")
    def inventory() -> dict:
        return get_read_only_inventory().model_dump(mode="json")

    @app.get("/operations/templates")
    def operation_templates() -> dict:
        return {"templates": get_operation_templates(), "physical_motion_requires_unlock": True}

    @app.get("/datasets")
    def datasets() -> dict:
        return {"datasets": [dataset.model_dump(mode="json") for dataset in list_dataset_summaries()]}

    @app.get("/policies/compatibility")
    def policy_compatibility() -> dict:
        return get_policy_compatibility().model_dump(mode="json")

    @app.get("/agent/tools")
    def agent_tools() -> dict:
        return {"tools": [tool.model_dump(mode="json") for tool in list_agent_tools()]}

    @app.get("/packaging/plan")
    def packaging_plan() -> dict:
        return get_packaging_plan().model_dump(mode="json")

    @app.get("/settings/api-keys")
    def api_key_settings() -> dict:
        return {
            "providers": [
                provider.model_dump(mode="json")
                for provider in list_api_key_providers(app.state.secret_last_four)
            ],
            "secrets_returned": False,
            "storage": "runtime_memory_until_os_keychain_integration",
        }

    @app.post("/settings/api-keys/{provider}")
    def update_api_key(provider: str, request: SecretUpdateRequest) -> dict:
        secret = request.value.get_secret_value()
        app.state.secret_values[provider] = secret
        app.state.secret_last_four[provider] = secret[-4:] if len(secret) >= 4 else "set"
        event = events.append(
            OperationEvent(
                source="settings",
                type="api_key_updated",
                payload={"provider": provider, "secret_returned": False},
            )
        )
        status = next(item for item in list_api_key_providers(app.state.secret_last_four) if item.provider == provider)
        return {"provider": status.model_dump(mode="json"), "event": event.model_dump(mode="json")}

    @app.post("/support-bundle/export")
    def support_bundle_export() -> dict:
        event = events.append(
            OperationEvent(
                source="support_bundle",
                type="support_bundle_prepared",
                payload={"secrets_included": False, "large_media_included": False},
            )
        )
        return {"ready": True, "secrets_included": False, "event": event.model_dump(mode="json")}

    @app.post("/stop")
    def stop() -> dict:
        event = events.append(
            OperationEvent(
                level="warning",
                source="safety",
                type="stop_requested",
                payload={"physical_motion_enabled": False, "hardware_disconnect_required": False},
            )
        )
        return {"accepted": True, "physical_motion_enabled": False, "event": event.model_dump(mode="json")}

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

    @app.post("/operations/request")
    def request_operation(request: OperationRequest) -> dict:
        operation = RobotOperation.from_request(request)
        safety = safety_gate.evaluate(operation)
        events.append(
            OperationEvent(
                operation_id=operation.id,
                source="safety_gate",
                type="operation_request_blocked" if not safety.allowed else "operation_request_ready",
                payload=safety.model_dump(mode="json"),
            )
        )
        return {"operation": operation.model_dump(mode="json"), "safety": safety.model_dump(mode="json")}

    @app.post("/operations/real-rollout/preflight")
    def real_rollout_preflight() -> dict:
        request = OperationRequest(
            type="run_policy_real",
            mode="real",
            requested_by="user",
            safety_level=SafetyLevel.PHYSICAL_MOTION,
            required_inputs=[
                "follower_port",
                "camera_config",
                "calibration_id",
                "policy_checkpoint",
                "feature_mapping",
                "duration_limit",
                "emergency_stop",
            ],
        )
        operation = RobotOperation.from_request(request)
        safety = safety_gate.evaluate(operation)
        return {"operation": operation.model_dump(mode="json"), "safety": safety.model_dump(mode="json")}

    desktop_dir = Path(__file__).resolve().parents[2] / "apps" / "desktop"
    if desktop_dir.exists():
        app.mount("/app", StaticFiles(directory=desktop_dir, html=True), name="desktop")

    return app


app = create_app()
