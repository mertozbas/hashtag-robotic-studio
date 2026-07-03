# Phase 1 Local Gateway Skeleton

Status: active

Phase 1 implemented the first non-actuating local gateway skeleton for Hashtag
Robotic Studio.

Durable facts:

- Gateway package: `services/local_gateway/`.
- Shared Python contracts: `packages/contracts/models.py`.
- Health endpoint: `GET /health` returns app, version, status, local fake mode,
  and `physical_motion_enabled=false`.
- Capability endpoint: `GET /capabilities` returns deterministic fake/local
  results and marks real SO101 teleop unavailable.
- Event endpoint: `GET /events` replays operation events as SSE.
- Fake operation endpoint: `POST /operations/fake` runs through `SafetyGate` and
  the operation state machine.
- `SafetyGate` blocks physical observation, physical motion, calibration write,
  and destructive data paths by default in phase 1.
- Tests cover gateway API, SafetyGate, and operation state machine behavior.

No serial ports, cameras, LeRobot drivers, Strands Robots real constructors, or
physical robot movement are used by the phase-1 gateway.
