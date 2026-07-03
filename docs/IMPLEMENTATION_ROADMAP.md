# Implementation Roadmap

Last updated: 2026-07-04

## Phase 0: Product Workspace

Status: current.

- product spec
- architecture
- safety model
- agent model
- UI system
- SDK strategy
- memory
- Codex skills
- git repo

## Phase 1: Local Gateway Prototype

Status: complete.

Goal: prove the backend contract before building the full desktop app.

Build:

- FastAPI gateway
- REST health endpoint
- WebSocket event stream
- device discovery endpoint
- camera discovery endpoint
- calibration status endpoint
- capability inventory endpoint
- fake operation state machine
- SafetyGate skeleton
- support bundle skeleton

No real motion.

## Phase 2: Web Cockpit Prototype

Status: next.

Goal: prove the UI information architecture.

Build:

- React/Vite or Next-style local UI
- Turkish/English i18n
- glass cockpit shell
- Home
- Devices
- Calibration
- Agent shell
- Diagnostics
- event stream viewer

No real motion.

## Phase 3: SO101 Read-only Integration

Goal: connect to local SO101 environment safely.

Build:

- package/version inventory
- LeRobot import check
- Strands Robots import check
- `Robot("so101", mode="sim", mesh=False)` smoke test
- calibration file discovery
- camera preview
- port discovery

No motor commands.

## Phase 4: Controlled Physical Workflows

Goal: first useful customer workflows.

Build:

- observation-only real connection
- bounded gripper/motor test
- leader/follower teleop session
- recording operation contract
- episode recording status
- emergency stop path
- operation log

Requires explicit hardware permission during development.

## Phase 5: Dataset Studio

Goal: make LeRobot dataset work visible and inspectable.

Build:

- dataset list
- metadata parser
- episode browser
- video preview
- frame scrubber
- state/action timeline
- quality checks
- export/upload action

## Phase 6: Policy Studio

Goal: prevent unsafe policy rollout through compatibility gates.

Build:

- checkpoint discovery
- config parser
- expected feature inspector
- mapping UI
- dry-run
- sim rollout
- real rollout preflight

## Phase 7: Agent-driven Robot Operation

Goal: product differentiator.

Build:

- Strands Agent runtime
- diagnostic tools
- simulation tools
- operation request tools
- bounded physical session tools
- tool-call stream
- camera context
- plan/execution trace
- agent permission scopes

## Phase 8: Packaging

Goal: customer install.

Build:

- Tauri/Electron decision
- bundled Python gateway
- app signing strategy
- Windows/macOS/Linux install tests
- update path
- support bundle export
