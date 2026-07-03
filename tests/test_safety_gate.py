from packages.contracts import OperationMode, OperationRequest, RobotOperation, SafetyLevel
from services.local_gateway.safety import SafetyGate


def test_safe_read_operation_is_allowed() -> None:
    operation = RobotOperation.from_request(OperationRequest(type="fake_inventory"))

    result = SafetyGate().evaluate(operation)

    assert result.allowed is True
    assert result.blockers == []


def test_physical_motion_is_blocked_by_default() -> None:
    operation = RobotOperation.from_request(
        OperationRequest(
            type="teleop_leader_follower",
            mode=OperationMode.REAL,
            safety_level=SafetyLevel.PHYSICAL_MOTION,
            required_inputs=["follower_port", "leader_port", "calibration_id", "duration_limit", "emergency_stop"],
        )
    )

    result = SafetyGate().evaluate(operation)

    assert result.allowed is False
    assert "physical_motion_disabled" in result.blockers
    assert "user_unlock_missing" in result.blockers
    assert "follower_port_missing" in result.blockers
    assert "emergency_stop_missing" in result.blockers


def test_physical_observe_is_not_enabled_in_phase_1() -> None:
    operation = RobotOperation.from_request(
        OperationRequest(type="connect_observation_only", mode=OperationMode.REAL, safety_level=SafetyLevel.PHYSICAL_OBSERVE)
    )

    result = SafetyGate().evaluate(operation)

    assert result.allowed is False
    assert result.blockers == ["physical_observe_not_enabled_in_phase_1"]
