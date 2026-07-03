---
title: "Phase 1 Local Gateway Skeleton"
type: backend
status: active
area: "local-gateway"
tags: ["phase-1", "fastapi", "safety-gate", "event-stream"]
created: 2026-07-04
updated: 2026-07-04
---

# Phase 1 Local Gateway Skeleton

## Summary

Phase 1 introduced the first runnable backend surface for Hashtag Robotic Studio:
a non-actuating FastAPI local gateway with shared contracts, deterministic fake
capabilities, SSE operation events, `SafetyGate`, and a fake operation state
machine.

## Context

The desktop cockpit should talk to a stable local gateway instead of calling
LeRobot or Strands Robots directly. Phase 1 proves that boundary without
touching real SO101 hardware.

## Decision Or Finding

- Gateway app: `services/local_gateway/app.py`.
- Contracts: `packages/contracts/models.py`.
- Fake inventory: `GET /capabilities`.
- Health: `GET /health`.
- Event stream: `GET /events` as SSE replay.
- Fake operation runner: `POST /operations/fake`.
- Physical observation, physical motion, calibration write, and destructive
  data are blocked in phase 1.

## Consequences

Phase 2 can build the cockpit UI against real HTTP/SSE contracts while still
remaining hardware-safe. Later phases can replace fake adapters with read-only
and then physical adapters without changing the UI boundary.

## Related

- `../../docs/ARCHITECTURE.md`
- `../../docs/SAFETY_MODEL.md`
- `../../services/local-gateway/README.md`
- `../../packages/contracts/README.md`
