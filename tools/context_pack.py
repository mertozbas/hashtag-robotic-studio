#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CORE_FILES = [
    "AGENTS.md",
    "docs/PROJECT_STATE.md",
    "docs/CURRENT_SPRINT.md",
    "docs/PRODUCT_SPEC.md",
    "docs/ARCHITECTURE.md",
    "docs/SAFETY_MODEL.md",
    "docs/AGENT_ROBOT_CONTROL_MODEL.md",
    "docs/UI_UX_SYSTEM.md",
    "docs/SDK_STRATEGY.md",
    "docs/AUTONOMOUS_CODEX_WORKFLOW.md",
    "roadmap/phases.json",
]


def read_text(path: Path, max_chars: int) -> str:
    if not path.exists():
        return ""
    text = path.read_text(encoding="utf-8", errors="replace").strip()
    if len(text) <= max_chars:
        return text
    return text[:max_chars].rstrip() + "\n..."


def load_phase(phase_id: str | None) -> dict:
    data = json.loads((ROOT / "roadmap/phases.json").read_text(encoding="utf-8"))
    if not phase_id:
        for phase in data["phases"]:
            if phase.get("status") in {"next", "active"}:
                return phase
        return {}
    for phase in data["phases"]:
        if phase["id"] == phase_id:
            return phase
    raise SystemExit(f"Unknown phase: {phase_id}")


def query_memory(query: str, top_k: int) -> str:
    python = ROOT / ".memory/.venv/bin/python"
    script = ROOT / ".memory/query.py"
    if not python.exists() or not script.exists():
        return "Memory unavailable. Install with `.memory/.venv/bin/pip install -r .memory/requirements.txt`."
    result = subprocess.run(
        [str(python), str(script), query, "--top-k", str(top_k), "--max-chars", "1200"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    return result.stdout.strip()


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a focused context pack for a Codex task.")
    parser.add_argument("--phase", default=None, help="Phase id such as phase-1.")
    parser.add_argument("--task", default="", help="Short task description.")
    parser.add_argument("--max-file-chars", type=int, default=2200)
    parser.add_argument("--memory-top-k", type=int, default=5)
    args = parser.parse_args()

    phase = load_phase(args.phase)
    query = " ".join(part for part in [phase.get("title", ""), phase.get("goal", ""), args.task] if part).strip()
    if not query:
        query = "Hashtag Robotic Studio current task"

    print("# Context Pack")
    print()
    print(f"Task: {args.task or '(not specified)'}")
    if phase:
        print(f"Phase: {phase['id']} - {phase['title']} [{phase['status']}]")
        print(f"Goal: {phase['goal']}")
        print("Acceptance:")
        for item in phase.get("acceptance", []):
            print(f"- {item}")
    print()

    print("## Memory")
    print()
    print(query_memory(query, args.memory_top_k))
    print()

    print("## Core Files")
    print()
    for rel in CORE_FILES:
        path = ROOT / rel
        if not path.exists():
            continue
        print(f"### {rel}")
        print()
        print(read_text(path, args.max_file_chars))
        print()


if __name__ == "__main__":
    main()

