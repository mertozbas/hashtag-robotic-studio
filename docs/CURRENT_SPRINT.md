# Current Sprint

Last updated: 2026-07-04

## Sprint Goal

Prepare Hashtag Robotic Studio as a Codex-ready product workspace: product spec, architecture, safety model, agent model, UI system, references, local memory, and project skills.

## Active Priorities

1. Keep product architecture local-first and avoid adding cloud infrastructure until a concrete customer need appears.
2. Define the agent-driven robot control model clearly: agent uses the robot through tools, contracts, safety gates, and logged operation runners.
3. Define the customer dashboard in enough detail to start implementation without redesigning the backend later.
4. Preserve SO101 physical safety rules from the lab system.
5. Track Strands Robots `0.4.1` as the target SDK version, but use isolated smoke tests before upgrading active environments.
6. Build memory and Codex skill files so future CLI sessions can continue with stable context.

## Not In Scope Yet

- Implementing the desktop app.
- Running hardware commands.
- Installing or upgrading Strands Robots in the parent lab `.venv`.
- Downloading models.
- Training policies.
- Uploading datasets.
- Creating a cloud backend.
- Publishing the repo.

## Definition Of Done

- `hashtag-robotic-studio/` contains product docs, safety docs, references, memory source files, Codex instructions, and local skill files.
- The memory seed manifest can ingest the initial product decisions.
- The folder is initialized as a git repository with the initial files committed.

## Added Autonomous Workflow Layer

- Added project-local Codex config for high-autonomy private workspace development.
- Added specialist Codex subagents for product architecture, UX, frontend, local gateway, SDK integration, agent ops, safety, QA, and docs/memory.
- Added `knowledge/` markdown vault for Obsidian-like project knowledge without depending on Obsidian.
- Added `roadmap/phases.json` for phase/task sequencing.
- Added `tools/context_pack.py`, `tools/next_task.py`, `tools/verify_phase.py`, and `tools/update_worklog.py`.
- Added autonomous workflow, expert agent, token efficiency, and version planning docs.
