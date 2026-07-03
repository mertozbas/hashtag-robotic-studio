# Codex Workspace Setup

Status: active

This workspace is structured to support future Codex CLI development.

Key files:

- `AGENTS.md`
- `docs/PROJECT_STATE.md`
- `docs/CURRENT_SPRINT.md`
- `docs/PRODUCT_SPEC.md`
- `docs/ARCHITECTURE.md`
- `docs/SAFETY_MODEL.md`
- `docs/AGENT_ROBOT_CONTROL_MODEL.md`
- `docs/UI_UX_SYSTEM.md`
- `docs/SDK_STRATEGY.md`
- `.memory/`
- `.codex/skills/`

Before non-trivial work, Codex should read state docs and query memory with a task-specific query.

Memory sources live under `memory/source`. The Chroma DB and virtualenv are local runtime artifacts and should not be committed.

