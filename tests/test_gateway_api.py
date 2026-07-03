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


def test_read_only_inventory_exposes_packages_ports_cameras_and_calibration_without_motor_commands() -> None:
    client = TestClient(create_app())

    response = client.get("/inventory")

    assert response.status_code == 200
    body = response.json()
    assert body["motor_commands_sent"] is False
    assert {package["name"] for package in body["packages"]} >= {"fastapi", "strands-robots", "lerobot"}
    assert all(port["safe_to_use"] is False for port in body["ports"])
    assert all(camera["safe_to_open"] is False for camera in body["cameras"])
    assert all(calibration["write_allowed"] is False for calibration in body["calibrations"])
    assert body["strands_sim_smoke"]["non_actuating"] is True


def test_physical_operation_request_is_blocked_without_unlock_and_inputs() -> None:
    client = TestClient(create_app())

    response = client.post(
        "/operations/request",
        json={
            "type": "teleop_leader_follower",
            "mode": "real",
            "safety_level": "physical_motion",
            "required_inputs": ["follower_port", "duration_limit", "emergency_stop"],
        },
    )

    assert response.status_code == 200
    body = response.json()
    assert body["safety"]["allowed"] is False
    assert "physical_motion_disabled" in body["safety"]["blockers"]
    assert "user_unlock_missing" in body["safety"]["blockers"]


def test_dataset_policy_agent_and_packaging_surfaces_are_safe_by_default() -> None:
    client = TestClient(create_app())

    datasets = client.get("/datasets").json()["datasets"]
    policy = client.get("/policies/compatibility").json()
    tools = client.get("/agent/tools").json()["tools"]
    packaging = client.get("/packaging/plan").json()
    stop = client.post("/stop").json()
    bundle = client.post("/support-bundle/export").json()

    assert datasets[0]["upload_explicit"] is True
    assert "dataset_path_not_selected" in datasets[0]["blockers"]
    assert policy["real_rollout_allowed"] is False
    assert "feature_mapping_blocked" in policy["blockers"]
    assert any(tool["name"] == "run_real_policy" and tool["enabled"] is False for tool in tools)
    assert packaging["support_bundle_export"] is True
    assert packaging["secrets_in_package"] is False
    assert stop["physical_motion_enabled"] is False
    assert bundle["secrets_included"] is False


def test_gateway_serves_desktop_cockpit_under_app_path() -> None:
    client = TestClient(create_app())

    response = client.get("/app/")

    assert response.status_code == 200
    assert "Hashtag Robotic Studio" in response.text
    assert 'data-screen="home"' in response.text


def test_api_key_settings_accept_secrets_without_returning_values() -> None:
    client = TestClient(create_app())

    initial = client.get("/settings/api-keys").json()
    updated = client.post("/settings/api-keys/huggingface", json={"value": "hf_1234567890abcdef"}).json()
    after = client.get("/settings/api-keys").json()

    assert initial["secrets_returned"] is False
    assert updated["provider"]["provider"] == "huggingface"
    assert updated["provider"]["connected"] is True
    assert updated["provider"]["last_four"] == "cdef"
    response_text = str(updated) + str(after)
    assert "hf_1234567890abcdef" not in response_text
    assert after["providers"][0]["secret_returned"] is False
