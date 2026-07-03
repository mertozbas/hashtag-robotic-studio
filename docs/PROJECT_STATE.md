# Project State

Last updated: 2026-07-04

## Current Goal

Complete roadmap skeleton is implemented through phase 8 without physical robot
movement. Next work is depth: replace fake/read-only adapters with isolated
SDK smoke checks, then customer packaging spike.

## Product Snapshot

- Product: Hashtag Robotic Studio.
- Target customer: SO101 robot buyer who should connect USB devices and operate the robot from a Turkish/English desktop app.
- Primary hardware: SO101 follower arm, optional SO101 leader arm, front camera, optional wrist camera.
- Product differentiator: agent-driven robot operation using Strands Agents and Strands Robots, with deterministic safety gates.
- Product stance: local-first. No Coolify/self-hosted PaaS layer in the product architecture.
- UI direction: serious glass cockpit, not a marketing landing page.

## Current Architecture Direction

- Desktop app shell: likely Tauri or Electron, to be decided after packaging spike.
- Frontend: React-style component app with i18n dictionaries.
- Local gateway: Python FastAPI service with REST and SSE/WebSocket event streams.
- Robot layer: adapter contracts over LeRobot and Strands Robots.
- Agent layer: Strands Agents with tool-call streaming and operation contracts.
- Safety layer: deterministic `SafetyGate` and operation state machines.
- Persistence: local config and SQLite-style app database.

## Implemented Product Skeleton

- Phase 1 adds a non-actuating FastAPI gateway package under
  `services/local_gateway/`.
- `GET /health` returns app/version/status and explicitly reports physical
  motion disabled.
- `GET /capabilities` returns deterministic fake/local capability inventory.
- `GET /events` replays operation events as SSE.
- `POST /operations/fake` runs fake operations through `SafetyGate` and a
  testable operation state machine.
- Physical observation, physical motion, calibration write, and destructive
  data paths are blocked by default in the phase-1 gateway.
- Phase 2 adds a static Turkish/English desktop cockpit prototype under
  `apps/desktop/` with Home, Devices, Calibration, Agent, and Diagnostics views.
- Phase 3 adds read-only package, port, camera, calibration, and optional sim
  inventory under `GET /inventory`.
- Phase 4 adds controlled physical workflow templates, stop endpoint, and
  SafetyGate preflight blocks for motion and calibration-write paths.
- Phase 5 adds dataset inventory and support for explicit upload/export
  semantics without deleting or uploading data.
- Phase 6 adds policy compatibility reporting with feature mapping blockers,
  explicit remote-code trust, and real-rollout denial by default.
- Phase 7 adds agent tool taxonomy and permission scopes with physical tools
  disabled until a bounded session exists.
- Phase 8 records the packaging plan surface and support bundle export skeleton
  with secrets excluded by default.
- The cockpit has been upgraded from a placeholder shell into a product-style
  SO101 readiness dashboard with arm connection preflight, live-control
  blockers, Hugging Face training setup, and API key vault settings.
- API key values can be submitted through the local gateway, but responses only
  return masked status. Persistent storage must use OS keychain in the packaging
  phase; secrets are not included in support bundles.

## Codex Development System

- Project-local autonomy config: `.codex/config.toml`.
- Specialist subagents: `.codex/agents/`.
- Prompt templates: `.codex/prompts/`.
- Obsidian-like local markdown vault: `knowledge/`.
- Machine-readable phase plan: `roadmap/phases.json`.
- Context and verification tools:
  - `tools/context_pack.py`
  - `tools/next_task.py`
  - `tools/verify_phase.py`
  - `tools/update_worklog.py`
- Token strategy: keep durable rules in `AGENTS.md`, long details in docs/vault/memory, and use targeted context packs.

## SDK Direction

- Target Strands Robots version for new work: `strands-robots==0.4.1`.
- Existing SO101 lab baseline outside this folder currently uses `strands-robots==0.4.0`.
- Upgrade rule: test `0.4.1` in an isolated environment before changing any working lab environment.
- LeRobot remains the source of truth for SO101 hardware, calibration, dataset schema, and proven workflows.

## Important Local Context

The parent lab folder contains useful prior work:

- `../docs/PROJECT_STATE.md`
- `../docs/STRANDS_ROBOTS_OPERATING_MODEL.md`
- `../docs/SO101_FEATURE_MAPPING.md`
- `../docs/ROBOT_PREFLIGHT_CHECKLIST.md`
- `../docs/ABSTRACTION_CARTOGRAPHY_STRANDS_ROBOTS_REVIEW_TR.md`
- `../docs/DASHBOARD_MVP_PLAN.md`

Do not treat those as product specs. Treat them as lab evidence and safety references.
