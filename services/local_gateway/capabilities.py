from __future__ import annotations

from packages.contracts import CapabilityInventory, OperationMode, RobotCapability, SafetyLevel


def get_fake_capability_inventory() -> CapabilityInventory:
    """Return deterministic local capabilities without probing hardware."""
    capabilities = [
        RobotCapability(
            name="gateway.health",
            provider="local_gateway",
            available=True,
            version="0.1.0",
            mode=OperationMode.FAKE,
            safety_level=SafetyLevel.SAFE_READ,
            evidence={"source": "static"},
        ),
        RobotCapability(
            name="so101.inventory.fake",
            provider="fake_adapter",
            available=True,
            version="0.1.0",
            mode=OperationMode.FAKE,
            safety_level=SafetyLevel.SAFE_READ,
            evidence={"hardware_probe": False, "physical_motion": False},
        ),
        RobotCapability(
            name="so101.teleop.leader_follower",
            provider="lerobot",
            available=False,
            version="unknown",
            mode=OperationMode.REAL,
            safety_level=SafetyLevel.PHYSICAL_MOTION,
            blockers=[
                "physical_motion_disabled",
                "follower_port_missing",
                "leader_port_missing",
                "calibration_id_missing",
                "emergency_stop_missing",
                "user_unlock_missing",
            ],
            evidence={"hardware_probe": False, "reason": "phase_1_non_actuating_gateway"},
        ),
    ]
    return CapabilityInventory(capabilities=capabilities)
