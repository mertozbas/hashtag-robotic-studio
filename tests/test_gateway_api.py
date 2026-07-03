from fastapi.testclient import TestClient

from services.local_gateway.app import create_app


def test_health_endpoint_returns_app_version_and_status() -> None:
    client = TestClient(create_app())

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "app": "hashtag-robotic-studio-gateway",
        "version": "0.1.0",
        "status": "ok",
        "mode": "local_fake",
        "physical_motion_enabled": False,
    }


def test_capabilities_are_deterministic_and_non_actuating() -> None:
    client = TestClient(create_app())

    response = client.get("/capabilities")

    assert response.status_code == 200
    body = response.json()
    assert body["mode"] == "fake"
    assert body["physical_motion_enabled"] is False
    names = [capability["name"] for capability in body["capabilities"]]
    assert names == ["gateway.health", "so101.inventory.fake", "so101.teleop.leader_follower"]
    teleop = body["capabilities"][2]
    assert teleop["available"] is False
    assert "physical_motion_disabled" in teleop["blockers"]


def test_fake_operation_endpoint_emits_operation_events() -> None:
    client = TestClient(create_app())

    response = client.post("/operations/fake", json={"type": "fake_diagnostic"})

    assert response.status_code == 200
    body = response.json()
    assert body["operation"]["status"] == "completed"
    assert body["safety"]["allowed"] is True
    assert [event["type"] for event in body["events"]] == [
        "operation_pending_preflight",
        "preflight_allowed",
        "operation_ready",
        "operation_running",
        "operation_completed",
    ]


def test_sse_event_stream_replays_operation_events() -> None:
    client = TestClient(create_app())
    client.post("/operations/fake", json={"type": "fake_diagnostic"})

    response = client.get("/events")

    assert response.status_code == 200
    assert "text/event-stream" in response.headers["content-type"]
    assert "event: operation_completed" in response.text
