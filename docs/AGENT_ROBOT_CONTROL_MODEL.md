# Agent Robot Control Model

Last updated: 2026-07-04

## Core Decision

The agent is allowed to operate the robot. That is one of the core product differentiators.

The agent is not allowed to bypass deterministic contracts, safety gates, operation runners, calibration requirements, feature mapping checks, motion limits, or emergency stop.

## Correct Mental Model

```text
User goal
  -> Strands Agent reasoning
  -> tool selection
  -> operation request
  -> SafetyGate
  -> deterministic runner
  -> LeRobot / Strands Robots / hardware
  -> event stream
  -> agent and UI observe result
```

## Agent Tool Classes

### Diagnostic Tools

No physical motion.

- inspect environment
- list robot capabilities
- list devices
- inspect calibration status
- inspect dataset metadata
- inspect policy config
- summarize logs
- generate support bundle

### Simulation Tools

No physical motion.

- create SO101 sim
- reset sim
- run policy dry-run
- run agent plan in sim
- inspect sim observation/action keys

### Preparation Tools

No physical motion, but may prepare an operation.

- create recording plan
- create teleop plan
- create rollout preflight
- select candidate mapping
- propose camera config

### Physical Operation Request Tools

Can lead to motion only after SafetyGate and user unlock.

- request teleop session
- request bounded motor test
- request dataset recording
- request real policy rollout
- request real agent task

### Physical Control Tools

Available only inside an approved bounded session.

- send high-level action
- move through approved policy runner
- control gripper within limits
- stop

These tools must be session-scoped. They expire when the operation ends.

## Tool-call Stream

The agent cockpit should show:

- user instruction
- agent plan summary
- selected tools
- tool arguments with sensitive fields masked
- SafetyGate result
- runner events
- final result

This stream is a trust feature. It should be readable by advanced users without overwhelming Easy Mode.

## Agent Memory

The product may keep local agent memory for:

- user's robot profile
- recurring setup issues
- preferred task labels
- known camera mapping
- local dataset history
- policy compatibility notes

Do not store:

- secrets
- private dataset images by default
- raw video embeddings without user consent
- unbounded logs

## Agent Failure Modes

The product must handle:

- hallucinated device names
- wrong port assumptions
- wrong camera key assumptions
- wrong action dimension
- unsupported SDK provider
- stale policy config
- user goal requiring impossible physical motion
- low-confidence vision
- long-running operations
- user cancels during execution

The right response is to block, ask for missing inputs, or run sim/dry-run first.

## User-facing Agent Behaviors

Good:

- "Follower port is not selected. I can only inspect devices right now."
- "This checkpoint expects `observation.images.front`, but the current camera is mapped as `front`. I need a mapping confirmation before real rollout."
- "I can run this in simulation first."
- "Recording can start after you confirm workspace clearance and set a 30 second duration."

Bad:

- "I will just try the first serial port."
- "The simulation worked, so real rollout is safe."
- "I changed calibration automatically."
- "I sent a motion command outside the approved session."

## Implementation Rule

The agent integration should be tested with fake/sim robot tools before real hardware tools are exposed.

