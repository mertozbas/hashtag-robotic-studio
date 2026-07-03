# Project State

Last updated: 2026-07-04

## Current Goal

Create the product and Codex operating system for Hashtag Robotic Studio before implementation begins.

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
- Local gateway: Python FastAPI service with REST and WebSocket event streams.
- Robot layer: adapter contracts over LeRobot and Strands Robots.
- Agent layer: Strands Agents with tool-call streaming and operation contracts.
- Safety layer: deterministic `SafetyGate` and operation state machines.
- Persistence: local config and SQLite-style app database.

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

