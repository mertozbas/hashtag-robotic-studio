from __future__ import annotations

from packages.contracts import RobotOperation, SafetyGateResult, SafetyLevel


PHYSICAL_BLOCKERS = {
    "follower_port": "follower_port_missing",
    "leader_port": "leader_port_missing",
    "camera_config": "camera_config_missing",
    "calibration_id": "calibration_id_missing",
    "duration_limit": "duration_limit_missing",
    "emergency_stop": "emergency_stop_missing",
    "workspace_clear": "workspace_not_confirmed",
}

RISKY_LEVELS = {
    SafetyLevel.PHYSICAL_MOTION,
    SafetyLevel.CALIBRATION_WRITE,
    SafetyLevel.DESTRUCTIVE_DATA,
}


class SafetyGate:
    def evaluate(self, operation: RobotOperation) -> SafetyGateResult:
        blockers: list[str] = []
        actions: list[str] = []

        for required in operation.required_inputs:
            if not operation.provided_inputs.get(required):
                blockers.append(PHYSICAL_BLOCKERS.get(required, f"{required}_missing"))
                actions.append(f"provide_{required}")

        if operation.safety_level == SafetyLevel.PHYSICAL_OBSERVE:
            blockers.append("physical_observe_not_enabled_in_phase_1")
            actions.append("request_observation_only_permission")

        if operation.safety_level in RISKY_LEVELS:
            blockers.append(f"{operation.safety_level.value}_disabled")
            actions.append("use_sim_or_fake_mode")
            if not operation.user_unlock:
                blockers.append("user_unlock_missing")
                actions.append("request_explicit_user_unlock")

        if (
            operation.requested_by.value == "agent"
            and operation.safety_level in RISKY_LEVELS
            and operation.agent_permission_scope not in {"run_bounded_motion_session", "record_dataset_session"}
        ):
            blockers.append("agent_permission_scope_insufficient")
            actions.append("grant_short_lived_agent_scope")

        unique_blockers = list(dict.fromkeys(blockers))
        unique_actions = list(dict.fromkeys(actions))
        allowed = not unique_blockers
        return SafetyGateResult(
            operation_id=operation.id,
            allowed=allowed,
            level="allowed" if allowed else "blocked",
            blockers=unique_blockers,
            required_user_actions=unique_actions,
        )
