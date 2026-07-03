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

    if not ok:
        raise SystemExit(1)
    print("Verification passed.")


if __name__ == "__main__":
    main()

