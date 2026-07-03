#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

BASE_CHECKS = [
    ["python3", "-m", "json.tool", "roadmap/phases.json"],
    ["python3", "-m", "json.tool", ".memory/seed_manifest.json"],
    ["python3", "-m", "py_compile", "tools/context_pack.py", "tools/next_task.py", "tools/verify_phase.py"],
    ["python3", "-m", "py_compile", ".memory/common.py", ".memory/query.py", ".memory/ingest.py", ".memory/ingest_all.py"],
]

PHASE_1_COMPILE_CHECK = [
    "python3",
    "-m",
    "py_compile",
    "packages/contracts/__init__.py",
    "packages/contracts/models.py",
    "services/local_gateway/app.py",
    "services/local_gateway/capabilities.py",
    "services/local_gateway/events.py",
    "services/local_gateway/operations.py",
    "services/local_gateway/safety.py",
    "services/local_gateway/inventory.py",
    "services/local_gateway/studio.py",
]

PHASE_REQUIREMENTS = {
    "phase-2": [
        "apps/desktop/index.html",
        "apps/desktop/styles.css",
        "apps/desktop/app.js",
        "tests/test_desktop_static.py",
    ],
    "phase-3": [
        "services/local_gateway/inventory.py",
        "tests/test_gateway_api.py",
    ],
    "phase-4": [
        "services/local_gateway/safety.py",
        "services/local_gateway/studio.py",
        "tests/test_safety_gate.py",
    ],
    "phase-5": [
        "services/local_gateway/studio.py",
        "tests/test_gateway_api.py",
    ],
    "phase-6": [
        "services/local_gateway/studio.py",
        "packages/contracts/models.py",
        "tests/test_gateway_api.py",
    ],
    "phase-7": [
        "services/local_gateway/studio.py",
        "services/local_gateway/app.py",
        "tests/test_gateway_api.py",
    ],
    "phase-8": [
        "services/local_gateway/studio.py",
        "apps/desktop/README.md",
        "tests/test_gateway_api.py",
    ],
}


def run(command: list[str]) -> bool:
    print("$ " + " ".join(command))
    result = subprocess.run(command, cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if result.stdout.strip():
        print(result.stdout.rstrip())
    if result.returncode != 0:
        print(f"FAILED: exit {result.returncode}")
        return False
    return True


def main() -> None:
    parser = argparse.ArgumentParser(description="Run local verification for a roadmap phase.")
    parser.add_argument("--phase", required=True)
    args = parser.parse_args()

    data = json.loads((ROOT / "roadmap/phases.json").read_text(encoding="utf-8"))
    phase = next((p for p in data["phases"] if p["id"] == args.phase), None)
    if not phase:
        raise SystemExit(f"Unknown phase: {args.phase}")

    print(f"Verifying {phase['id']}: {phase['title']}")
    ok = True
    for command in BASE_CHECKS:
        ok = run(command) and ok

    if args.phase == "phase-0":
        required = [
            "AGENTS.md",
            "docs/PRODUCT_SPEC.md",
            "docs/ARCHITECTURE.md",
            "docs/SAFETY_MODEL.md",
            "docs/AGENT_ROBOT_CONTROL_MODEL.md",
            "docs/UI_UX_SYSTEM.md",
            ".codex/config.toml",
            "knowledge/00-index/README.md",
        ]
        for rel in required:
            exists = (ROOT / rel).exists()
            print(f"{'OK' if exists else 'MISSING'} {rel}")
            ok = exists and ok

    if args.phase == "phase-1":
        required = [
            "pyproject.toml",
            "packages/contracts/models.py",
            "services/local_gateway/app.py",
            "services/local_gateway/capabilities.py",
            "services/local_gateway/events.py",
            "services/local_gateway/operations.py",
            "services/local_gateway/safety.py",
            "tests/test_gateway_api.py",
            "tests/test_operation_state_machine.py",
            "tests/test_safety_gate.py",
        ]
        for rel in required:
            exists = (ROOT / rel).exists()
            print(f"{'OK' if exists else 'MISSING'} {rel}")
            ok = exists and ok
        ok = run(PHASE_1_COMPILE_CHECK) and ok
        ok = run(["python3", "-m", "pytest"]) and ok

    if args.phase in PHASE_REQUIREMENTS:
        for rel in PHASE_REQUIREMENTS[args.phase]:
            exists = (ROOT / rel).exists()
            print(f"{'OK' if exists else 'MISSING'} {rel}")
            ok = exists and ok
        ok = run(PHASE_1_COMPILE_CHECK) and ok
        ok = run(["python3", "-m", "pytest"]) and ok

    if not ok:
        raise SystemExit(1)
    print("Verification passed.")


if __name__ == "__main__":
    main()
