# Current Sprint

Last updated: 2026-07-04

## Sprint Goal

Roadmap skeleton through phase 8 is now complete without physical robot
movement. The next sprint should deepen the implementation behind the completed
contracts instead of adding more placeholder surface.

## Active Priorities

1. Run an isolated Strands Robots `0.4.1` smoke environment before any SDK upgrade.
2. Choose and test Tauri vs Electron packaging for the bundled Python gateway.
3. Replace fake inventory with read-only adapters while preserving no-motion guarantees.
4. Preserve SO101 physical safety rules from the lab system.
5. Keep agent-driven robot control behind tools, contracts, safety gates, and logged operation runners.
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

- All roadmap phase verification commands pass.
- The next implementation branch selects a packaging shell or read-only SDK
  adapter target.
- Physical controls remain visually and technically blocked unless Mert gives
  explicit current-turn hardware permission.

## Completed Phase 1

- Added shared Python contracts under `packages/contracts/`.
- Added non-actuating FastAPI gateway under `services/local_gateway/`.
- Added deterministic fake capability inventory.
- Added SSE operation event replay.
- Added `SafetyGate` and fake operation state machine.
- Added unit/API tests and phase-1 verification coverage.

## Completed Phase 2-8 Skeleton

- Added static Turkish/English cockpit shell under `apps/desktop/`.
- Added read-only inventory endpoint for packages, ports, cameras, calibration,
  and optional sim smoke status.
- Added operation templates, stop endpoint, and real-rollout preflight blocker.
- Added dataset, policy compatibility, agent tool, packaging plan, and support
  bundle endpoints.
- Added verification coverage for phases 2 through 8.
- No physical robot movement, calibration write, dataset deletion, checkpoint
  deletion, model download, training job, Docker pull, or public publish was run.

## Added Autonomous Workflow Layer

- Added project-local Codex config for high-autonomy private workspace development.
- Added specialist Codex subagents for product architecture, UX, frontend, local gateway, SDK integration, agent ops, safety, QA, and docs/memory.
- Added `knowledge/` markdown vault for Obsidian-like project knowledge without depending on Obsidian.
- Added `roadmap/phases.json` for phase/task sequencing.
- Added `tools/context_pack.py`, `tools/next_task.py`, `tools/verify_phase.py`, and `tools/update_worklog.py`.
- Added autonomous workflow, expert agent, token efficiency, and version planning docs.
