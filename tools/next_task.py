#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    data = json.loads((ROOT / "roadmap/phases.json").read_text(encoding="utf-8"))
    phases = data["phases"]
    current = next((p for p in phases if p.get("status") == "active"), None)
    next_phase = current or next((p for p in phases if p.get("status") == "next"), None)
    if not next_phase:
        next_phase = next((p for p in phases if p.get("status") == "planned"), None)
    if not next_phase:
        print("No next phase found.")
        return

    print(f"{next_phase['id']}: {next_phase['title']}")
    print()
    print(next_phase["goal"])
    print()
    print("Acceptance:")
    for item in next_phase.get("acceptance", []):
        print(f"- {item}")
    print()
    print("Suggested Codex prompt:")
    print(
        f"Run {next_phase['id']} ({next_phase['title']}) from roadmap/phases.json. "
        "Use tools/context_pack.py first, implement, test, update docs/memory if needed, commit, and report the next task. "
        "No physical robot movement unless explicitly authorized."
    )


if __name__ == "__main__":
    main()

