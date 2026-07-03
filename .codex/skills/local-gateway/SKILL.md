---
name: local-gateway
description: Use when implementing or reviewing the Hashtag Robotic Studio local FastAPI gateway, robot contracts, adapters, event streams, SafetyGate, or operation state machines.
---

# Local Gateway Skill

Use this skill when implementing the FastAPI local gateway, contracts, adapters, event streams, SafetyGate, or operation state machines.

## Required Reads

- `docs/ARCHITECTURE.md`
- `docs/SAFETY_MODEL.md`
- `docs/AGENT_ROBOT_CONTROL_MODEL.md`
- `services/local-gateway/README.md`
- `packages/contracts/README.md`

## Rules

- UI must talk to the gateway, not directly to LeRobot or Strands Robots.
- Physical operations must be represented as typed `RobotOperation`s.
- SafetyGate blocks by default when required inputs are missing.
- Use fake/sim adapters before real hardware.
- No physical motion without explicit current-turn permission.

## Expected Verification

- contract tests
- state machine tests
- SafetyGate tests
- fake operation event stream tests
