from __future__ import annotations

import importlib.metadata
import sys
from pathlib import Path

from packages.contracts import CalibrationStatus, CameraCandidate, DeviceInventory, PackageStatus, PortCandidate


def _package(name: str) -> PackageStatus:
    try:
        version = importlib.metadata.version(name)
        return PackageStatus(name=name, installed=True, version=version)
    except importlib.metadata.PackageNotFoundError:
        return PackageStatus(name=name, installed=False)


def get_read_only_inventory() -> DeviceInventory:
    port_globs = ["/dev/cu.*", "/dev/tty.*"] if sys.platform != "win32" else []
    ports: list[PortCandidate] = []
    for pattern in port_globs:
        for path in sorted(Path("/").glob(pattern.lstrip("/"))):
            ports.append(PortCandidate(path=str(path), safe_to_use=False))

    return DeviceInventory(
        packages=[
            _package("fastapi"),
            _package("uvicorn"),
            _package("strands-robots"),
            _package("strands-agents"),
            _package("lerobot"),
        ],
        ports=ports,
        cameras=[
            CameraCandidate(id="front", label="Front camera candidate", available=False),
            CameraCandidate(id="wrist", label="Wrist camera candidate", available=False),
        ],
        calibrations=[
            CalibrationStatus(robot_id="mert_follower", role="follower", present=False),
            CalibrationStatus(robot_id="mert_leader", role="leader", present=False),
        ],
        strands_sim_smoke={
            "optional": True,
            "executed": False,
            "non_actuating": True,
            "reason": "phase_3_does_not_install_or_import_optional_sdk",
        },
    )
