# Product Spec: Hashtag Robotic Studio

Last updated: 2026-07-04

## One-line Product

Hashtag Robotic Studio is a local-first desktop application for SO101 owners to set up, control, record, inspect, train/evaluate workflows, and run agent-driven robot operations without using a terminal.

## Positioning

This is not just a LeRobot UI and not just a Strands demo dashboard. It is the customer operating system shipped with Hashtag Robotics SO101 robots.

The product should make SO101 feel like a packaged robot product:

- connect the follower and optional leader via USB
- detect cameras
- verify calibration
- start safe teleoperation
- record LeRobot-compatible datasets
- review dataset quality
- validate policy compatibility
- run simulation or dry-run checks
- let a Strands agent operate the robot through explicit tools
- generate diagnostics and support bundles

## Non-negotiable Product Principles

1. Local-first:
   Core robot workflows must run on the customer's PC without a hosted server.

2. Agent-driven:
   Agent robot operation is a flagship feature. The app should expose a serious agent cockpit with tool-call streaming, robot state, camera context, operation state, and safety status.

3. Deterministic safety:
   LLMs reason and choose tools; deterministic runners enforce hardware limits, calibration requirements, timeouts, action constraints, logging, and emergency stop behavior.

4. LeRobot compatibility:
   Datasets, calibration, SO101 driver semantics, and baseline record/train/eval workflows must remain compatible with LeRobot.

5. Strands orchestration:
   Strands Robots and Strands Agents should be the product orchestration layer around robots, policies, simulation, agent tools, and future mesh/ROS capabilities.

6. Turkish first, English available:
   Turkish is the default product language. English is selectable and must be maintained through the same i18n system.

7. No Coolify dependency:
   No self-hosted PaaS layer is part of the core architecture. Policy downloads, Hugging Face login, dataset uploads, updates, and support export can be implemented inside the app directly.

## Target Users

### Customer Operator

Bought an SO101 from Hashtag Robotics. Wants to plug it into a PC and start safely. Does not want terminal commands or Python environment issues.

Needs:

- guided setup
- device detection
- calibration status
- safe motion tests
- teleoperation
- simple task recording
- support diagnostics

### Builder / Researcher

Wants to collect datasets, inspect episodes, train/evaluate policies, and iterate on workflows.

Needs:

- raw device details
- camera previews
- dataset metadata
- policy compatibility checks
- sim/dry-run
- logs
- tool-call traces
- export/import

### Agent Developer

Wants to build Strands agent behaviors over SO101.

Needs:

- tool registry
- capability detection
- event stream
- operation contracts
- dry-run mode
- sandboxed test tools
- safety gate observability

### Support / QA

Needs to diagnose customer setup problems without seeing secrets.

Needs:

- support bundle
- masked config
- package versions
- port/camera inventory
- calibration presence
- recent logs
- dataset integrity result

## Modes

### Easy Mode

Default customer path.

- guided onboarding
- no raw CLI detail
- clear device status
- low-risk teleoperation
- demo recording
- diagnostics

### Lab Mode

For robotics iteration.

- dataset studio
- policy studio
- simulation
- replay
- raw mappings
- adapter status

### Developer Mode

For SDK and agent work.

- capability registry
- tool-call stream
- raw events
- contract schemas
- package versions
- feature mapping
- REST/WebSocket debug views

## First-run Flow

1. Language selection:
   - Turkish
   - English

2. Robot profile:
   - SO101 follower only
   - SO101 leader + follower
   - simulation only

3. Device discovery:
   - follower port candidates
   - leader port candidates
   - camera devices
   - OS permissions

4. Calibration check:
   - follower calibration exists
   - leader calibration exists when needed
   - calibration backup available
   - calibration age/status

5. Camera preview:
   - front camera
   - optional wrist camera
   - resolution/FPS
   - latency
   - frame health

6. Safety check:
   - workspace clear
   - power state
   - motor lock state
   - emergency stop path
   - motion duration limit

7. Observation-only connection:
   - no motor movement
   - read robot status where available
   - confirm driver import and port open behavior

8. Bounded motion test:
   - requires explicit operator unlock
   - short duration
   - low speed
   - visible stop

9. Dashboard ready:
   - customer lands in the main cockpit

## Main Navigation

- `Başlangıç` / `Home`
- `Cihazlar` / `Devices`
- `Kalibrasyon` / `Calibration`
- `Canlı Kontrol` / `Live Control`
- `Agent`
- `Kayıt` / `Recording`
- `Datasetler` / `Datasets`
- `Policyler` / `Policies`
- `Simülasyon` / `Simulation`
- `Çalıştır` / `Run`
- `Tanılama` / `Diagnostics`
- `Ayarlar` / `Settings`

## Core Screens

### Home

Purpose: fast operational status.

Shows:

- robot readiness
- device status
- calibration status
- camera status
- safety gate status
- last operation
- open blockers
- recommended next action

### Devices

Purpose: inventory and assignment.

Shows:

- follower candidates
- leader candidates
- camera list
- selected device mapping
- OS permission status
- reconnect and refresh actions

Rules:

- never assume ports
- show candidate confidence
- distinguish connected, selected, verified, and blocked

### Calibration

Purpose: inspect, backup, restore, and guided calibration.

Shows:

- calibration ids
- file paths
- existence checks
- backup list
- joint zero/limit metadata when available
- validation result

Rules:

- calibration write requires explicit operation unlock
- backups before overwrite
- restore is separate from calibrate
- guided calibration must show physical pose instructions

### Live Control

Purpose: manual robot operation.

Controls:

- leader/follower teleop
- optional keyboard/gamepad control
- speed limiter
- gripper test
- motor enable/disable
- timed session
- emergency stop

Rules:

- all physical control paths require SafetyGate approval
- session duration limit required
- logs and events are always recorded

### Agent

Purpose: flagship agent-driven robot cockpit.

Shows:

- chat/voice command
- camera context selection
- tool-call stream
- operation state
- safety status
- robot event log
- agent memory/context summary
- manual approve/deny when needed

Capabilities:

- diagnose setup
- plan a task
- run sim checks
- request teleop/record/rollout operations
- operate robot through approved tools
- explain blockers
- generate support summary

### Recording

Purpose: LeRobot-compatible dataset collection.

Inputs:

- task text
- dataset repo/path
- episode count
- episode duration
- FPS
- camera keys
- codec
- upload disabled/enabled
- leader/follower selection

Shows:

- live video
- episode timer
- dropped frames
- action/state stream health
- recording status
- current blocker

Rules:

- upload requires explicit user action
- H.264 preferred for local recordings unless storage constraints justify otherwise
- dataset schema must be visible in Lab/Developer mode

### Datasets

Purpose: inspect and validate data.

Shows:

- dataset list
- episodes
- frames
- FPS
- camera keys
- codecs
- metadata
- video preview
- state/action timeline
- quality checks
- export/upload controls

Quality checks:

- missing video
- missing parquet rows
- camera key mismatch
- action dimension mismatch
- corrupted episode
- short episode
- frame drops

### Policies

Purpose: manage local and downloadable policies.

Sources:

- local checkpoint
- Hugging Face repo
- built-in demo manifest

Checks:

- policy family
- model provider
- expected image keys
- expected state/action features
- action dimension
- normalization/scaling
- gripper convention
- device target
- remote code requirement

Rules:

- no real rollout until compatibility is resolved
- remote code trust must be explicit

### Simulation

Purpose: sim-first validation.

Capabilities:

- Strands `Robot("so101", mode="sim", mesh=False)` smoke check
- policy dry-run
- task scene replay
- action dimension test
- camera key mapping test
- synthetic episode preview

Rules:

- simulation success is not proof of real-robot safety
- sim/real mapping must be displayed when relevant

### Run

Purpose: execute real policy or agent task on hardware.

This is the strictest screen.

Requires:

- selected operation
- follower port
- camera config
- calibration id
- policy/checkpoint or agent plan
- feature mapping
- action limits
- duration/step limit
- emergency stop path
- operator unlock

### Diagnostics

Purpose: support and failure analysis.

Outputs:

- masked config
- app version
- package versions
- OS details
- device inventory
- camera inventory
- calibration presence
- recent logs
- recent operation events
- dataset integrity summary
- support bundle zip

Rules:

- never include tokens/secrets by default
- ask before including large datasets or videos

### Settings

Purpose: stable user preferences and advanced controls.

Contains:

- language
- theme
- data directories
- Hugging Face login
- model cache path
- default camera keys
- developer mode toggle
- safety defaults
- log retention

## MVP Scope

The first implementation should include:

- Turkish/English i18n
- device discovery
- camera preview
- calibration existence/status
- local gateway with REST/WebSocket
- home dashboard
- safety gate model
- operation event stream
- agent cockpit shell
- teleoperation operation contract
- recording operation contract
- dataset inventory and preview
- policy compatibility inspection
- simulation smoke check
- diagnostics/support bundle

Defer:

- training UI
- automatic cloud sync
- fleet management
- remote mesh control
- full ROS/MoveIt2 integration
- app store distribution
- multi-robot scheduling

## Open Product Questions

- Tauri or Electron for packaging Python plus camera/robot dependencies?
- How much of LeRobot CLI should be wrapped versus imported directly?
- Should the first customer release include real autonomous rollout, or keep it behind Developer Mode?
- What is the default SO101 demo task shipped with the product?
- Should voice be in MVP or second release?
- What exact support bundle policy is acceptable for customer privacy?

