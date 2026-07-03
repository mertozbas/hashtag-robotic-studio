# Autonomous Codex Workflow

Status: active

Hashtag Robotic Studio now has a Codex development system for long autonomous implementation loops.

Core components:

- `.codex/config.toml` sets high-autonomy local defaults for this trusted private workspace.
- `.codex/agents/` defines specialist subagents for product, UX, frontend, local gateway, SDK, agent ops, safety, QA, and docs/memory.
- `.codex/prompts/` contains reusable phase and review prompts.
- `knowledge/` is a local markdown vault inspired by Obsidian but without an Obsidian dependency.
- `roadmap/phases.json` sequences implementation phases.
- `tools/context_pack.py`, `tools/next_task.py`, `tools/verify_phase.py`, and `tools/update_worklog.py` support focused context, next-task discovery, verification, and worklogs.

Hard stops remain: physical robot movement, calibration overwrite, destructive dataset/checkpoint changes, long training/model downloads, Docker pulls, external account actions, and public publishing.

