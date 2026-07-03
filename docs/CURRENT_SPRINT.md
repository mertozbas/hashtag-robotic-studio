# Current Sprint

Last updated: 2026-07-04

## Sprint Goal

Move from Codex-ready product workspace into the first runnable local product
skeleton: a non-actuating gateway first, then a Turkish/English desktop cockpit.

## Active Priorities

1. Build phase 2 desktop cockpit against the phase 1 local gateway contracts.
2. Keep product architecture local-first and avoid adding cloud infrastructure until a concrete customer need appears.
3. Keep agent-driven robot control behind tools, contracts, safety gates, and logged operation runners.
4. Preserve SO101 physical safety rules from the lab system.
5. Track Strands Robots `0.4.1` as the target SDK version, but use isolated smoke tests before upgrading active environments.
6. Keep memory and knowledge notes compact as implementation decisions land.

## Not In Scope Yet

- Running hardware commands.
- Installing or upgrading Strands Robots in the parent lab `.venv`.
- Downloading models.
- Training policies.
- Uploading datasets.
- Creating a cloud backend.
- Publishing the repo.

## Definition Of Done

- Phase 1 gateway verification passes.
- Phase 2 cockpit shell exists with Turkish/English dictionaries.
- UI reads health/capability/events from the local gateway.
- Physical controls remain visually and technically blocked unless explicitly
  added in a later hardware phase.

## Completed Phase 1

- Added shared Python contracts under `packages/contracts/`.
- Added non-actuating FastAPI gateway under `services/local_gateway/`.
- Added deterministic fake capability inventory.
- Added SSE operation event replay.
- Added `SafetyGate` and fake operation state machine.
- Added unit/API tests and phase-1 verification coverage.

## Added Autonomous Workflow Layer

- Added project-local Codex config for high-autonomy private workspace development.
- Added specialist Codex subagents for product architecture, UX, frontend, local gateway, SDK integration, agent ops, safety, QA, and docs/memory.
- Added `knowledge/` markdown vault for Obsidian-like project knowledge without depending on Obsidian.
- Added `roadmap/phases.json` for phase/task sequencing.
- Added `tools/context_pack.py`, `tools/next_task.py`, `tools/verify_phase.py`, and `tools/update_worklog.py`.
- Added autonomous workflow, expert agent, token efficiency, and version planning docs.
