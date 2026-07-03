# Safety Model

Last updated: 2026-07-04

## Product Safety Position

Hashtag Robotic Studio controls physical hardware. Treat this as physical-world software.

The agent can operate the robot, but only through explicit robot tools, operation contracts, deterministic safety gates, and bounded runners.

## Safety Layers

### Layer 1: UI Intent

The UI must distinguish:

- inspect-only actions
- simulation actions
- physical connection actions
- physical motion actions
- calibration-write actions
- autonomous/agent actions
- destructive data actions

The visual treatment must make physical and destructive actions obvious.

### Layer 2: Operation Contract

Every risky action becomes a `RobotOperation` with typed requirements.

Examples:

- `connect_observation_only`
- `teleop_leader_follower`
- `record_dataset`
- `calibrate_follower`
- `restore_calibration`
- `simulate_policy`
- `run_policy_real`
- `agent_task_real`

### Layer 3: SafetyGate

The SafetyGate evaluates:

- selected operation
- hardware mode
- follower port
- leader port when required
- camera config
- calibration presence
- policy/checkpoint compatibility
- feature mapping
- duration/step limit
- speed/action limits
- emergency stop path
- workspace confirmation
- user unlock
- agent permission scope

### Layer 4: Deterministic Runner

The runner enforces:

- timeout
- stop signal
- max speed/action delta
- joint limits where known
- gripper bounds
- no movement after stop
- logging
- cleanup on error

### Layer 5: Hardware / Driver

LeRobot and Strands Robots interact with the actual device. The app should not fork or patch low-level driver behavior unless necessary. Product-level guarantees belong in contracts and runners.

## Permission Classes

### Safe Read

Allowed without extra confirmation:

- read docs/config
- inspect package versions
- query memory
- list local datasets
- list local checkpoints
- discover ports/cameras
- read calibration file presence
- run UI-only validation

### Simulation

Allowed after user selects sim action:

- `Robot("so101", mode="sim", mesh=False)` smoke test
- simulation reset
- policy dry-run in simulation
- synthetic dataset preview

### Physical Observe

Requires explicit connection intent:

- open serial port without motion
- read passive state where supported
- open camera preview
- validate calibration presence

### Physical Motion

Requires explicit current operation unlock:

- teleoperation
- motor test
- gripper test
- replay
- real policy rollout
- agent physical task execution

### Calibration Write

Requires stronger confirmation:

- backup existing calibration
- show path
- show affected robot role
- require typed or button-held confirmation
- write only after explicit user action

### Destructive Data

Requires explicit confirmation:

- delete dataset
- delete checkpoint
- overwrite dataset
- clear logs
- clear support bundles

## Agent Permission Scopes

The agent should have scoped permissions, not global trust.

Suggested scopes:

- `diagnose_only`
- `simulate_only`
- `prepare_operation`
- `request_physical_motion`
- `run_bounded_motion_session`
- `record_dataset_session`
- `run_policy_session`

Default scope: `diagnose_only`.

Agent may ask for a higher scope. The UI grants it only for a short operation or time window.

## Emergency Stop

The UI must always expose:

- visual emergency stop
- keyboard stop shortcut
- backend stop endpoint
- runner stop token
- hardware disconnect fallback where available

Rules:

- stop must be available while the app is busy
- stop must not depend on agent cooperation
- stop events are logged
- after stop, require re-arm before motion

## Motion Limits

Every physical motion operation must define:

- max duration
- max action delta or speed scale
- max frequency
- allowed joints
- gripper bounds
- stop behavior

Unknown joint units or gripper convention must block real rollout.

## Rollout Blockers

Block real autonomous/agent rollout if any are unknown:

- follower port
- camera config
- calibration id
- selected policy or agent tool plan
- image key mapping
- state/action feature order
- action dimension
- unit conversion
- gripper range/direction
- duration or step limit
- emergency stop path

## Logging Rules

Log:

- operation request
- preflight result
- user unlock
- agent tool calls
- runner start/stop
- errors
- stop events
- final summary

Never log secrets by default.

## Safety UX Rules

- `STOP` must be solid, high contrast, and always visible during physical operations.
- Critical action buttons must not rely only on glass transparency.
- Use Turkish copy that is direct and unambiguous.
- Do not hide blockers. Show the exact missing input or failed check.
- Use amber for incomplete preflight, red for blocked/danger/stop, green only for verified ready.

