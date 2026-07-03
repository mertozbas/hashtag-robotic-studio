# Architecture

Last updated: 2026-07-04

## Summary

Hashtag Robotic Studio should be built as a local-first desktop app with a deterministic local robot gateway. The frontend is a cockpit. The backend is the robot runtime. Strands Agents and Strands Robots are first-class, but all physical operations go through explicit contracts and safety gates.

## Runtime Shape

```text
Desktop Shell
  React UI
  i18n dictionaries
  local auth/session
  camera/robot cockpit

Local Gateway
  FastAPI REST API
  WebSocket event stream
  operation state machine
  safety gate
  adapter registry
  local persistence

Agent Runtime
  Strands Agents
  robot tools
  diagnostics tools
  dataset tools
  policy tools
  tool-call/event streaming

Robot Runtime
  Strands Robots adapter
  LeRobot adapter
  camera adapter
  dataset adapter
  policy adapter
  simulation adapter

Hardware/Assets
  SO101 follower
  SO101 leader
  cameras
  calibration files
  datasets
  checkpoints
```

## Backend Boundary

The UI must never call LeRobot or Strands Robots directly. It talks to the local gateway through stable contracts.

This prevents a future SDK change from forcing a UI rewrite.

## Key Contracts

### RobotCapability

Represents what the current machine can do.

```json
{
  "name": "so101.teleop.leader_follower",
  "provider": "lerobot",
  "available": true,
  "version": "0.5.x",
  "mode": "real",
  "safety_level": "physical_motion",
  "blockers": [],
  "evidence": {
    "package": "lerobot",
    "ports": ["selected_follower", "selected_leader"],
    "calibration": "present"
  }
}
```

### RobotOperation

Represents a user or agent-requested workflow.

```json
{
  "id": "op_...",
  "type": "teleop",
  "mode": "real",
  "requested_by": "agent | user | system",
  "status": "pending_preflight",
  "safety_level": "physical_motion",
  "required_inputs": [
    "follower_port",
    "leader_port",
    "calibration_id",
    "duration_limit",
    "emergency_stop"
  ],
  "limits": {
    "max_duration_s": 60,
    "max_speed_scale": 0.25
  }
}
```

### SafetyGateResult

Represents whether an operation may run.

```json
{
  "operation_id": "op_...",
  "allowed": false,
  "level": "blocked",
  "blockers": [
    "leader_port_missing",
    "workspace_not_confirmed"
  ],
  "required_user_actions": [
    "select_leader_port",
    "confirm_workspace_clear"
  ]
}
```

### RobotEvent

All runtime state is evented.

```json
{
  "ts": "2026-07-04T12:00:00Z",
  "operation_id": "op_...",
  "level": "info",
  "source": "safety_gate",
  "type": "preflight_blocked",
  "payload": {
    "blockers": ["camera_missing"]
  }
}
```

### FeatureMapping

Represents policy/dataset/runtime compatibility.

```json
{
  "robot": "so101",
  "camera_keys": {
    "runtime_front": "front",
    "dataset_front": "observation.images.front",
    "policy_front": "observation.images.front"
  },
  "state_features": [
    "shoulder_pan.pos",
    "shoulder_lift.pos",
    "elbow_flex.pos",
    "wrist_flex.pos",
    "wrist_roll.pos",
    "gripper.pos"
  ],
  "action_dimension": 6,
  "unit_status": "verified | assumed | blocked"
}
```

## Adapter Responsibilities

### StrandsRobotsAdapter

- construct sim robots
- construct real robot only after explicit approval path
- expose provider capabilities
- run policy dry-runs where supported
- manage Strands tool integration
- surface SDK version and missing extras

### LeRobotAdapter

- device/calibration semantics
- SO101 leader/follower workflows
- dataset recording
- dataset metadata inspection
- baseline policy config inspection
- training/eval command construction

### CameraAdapter

- discover cameras
- open previews
- measure FPS/latency
- provide frame health
- map runtime camera names to dataset keys

### DatasetAdapter

- list datasets
- inspect metadata
- validate episodes
- preview video
- timeline state/action rows
- export/upload when explicitly requested

### PolicyAdapter

- list local checkpoints
- inspect configs
- validate image/state/action mappings
- check device requirements
- check remote-code requirements
- create dry-run plans

### AgentAdapter

- own Strands Agent lifecycle
- register tools
- stream tool calls
- route operation requests through SafetyGate
- summarize failures
- never bypass operation contracts

## Operation State Machine

```text
draft
  -> pending_preflight
  -> blocked
  -> awaiting_user_unlock
  -> ready
  -> running
  -> stopping
  -> completed
  -> failed
  -> aborted
```

Rules:

- Physical operations cannot skip `pending_preflight`.
- Agent-requested physical operations cannot skip `awaiting_user_unlock` unless the user has configured a short-lived explicit session permission.
- `stopping` must be reachable from every running physical state.
- All transitions emit `RobotEvent`.

## Persistence

Use local persistence for:

- user preferences
- selected language
- robot profile
- selected ports/cameras
- calibration metadata cache
- operation history
- support-bundle index
- policy registry cache
- dataset registry cache

Do not store secrets in plain text. Use OS credential storage where possible.

## Packaging Strategy

Start with a packaging spike before committing:

- Option A: Tauri + React + bundled Python gateway.
- Option B: Electron + React + bundled Python gateway.

Decision criteria:

- easiest customer install
- macOS/Windows/Linux feasibility
- camera and USB permission behavior
- bundled Python reliability
- auto-update path
- binary size
- developer speed

Do not let the desktop shell choice leak into robot contracts.

