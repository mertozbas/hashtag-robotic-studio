---
title: "Phase 2-8 Product Skeleton"
type: worklog
status: active
area: "roadmap"
tags: ["phase-2", "phase-3", "phase-4", "phase-5", "phase-6", "phase-7", "phase-8"]
created: 2026-07-04
updated: 2026-07-04
---

# Phase 2-8 Product Skeleton

## Summary

Roadmap phases 2 through 8 were completed as safe, no-motion product skeletons.
The implementation adds a static cockpit UI and expands the local gateway with
read-only and fake surfaces for inventory, operations, datasets, policy
compatibility, agent tools, packaging, support bundles, and stop events.

## Context

The user asked to complete all phases. Hardware actions remain hard stops, so
phase 4 physical workflows are implemented as operation templates and
SafetyGate preflights, not live robot movement.

## Decision Or Finding

- Phase 2: static cockpit in `apps/desktop/`, Turkish default with English
  toggle, gateway health/capability/events/inventory reads.
- Phase 3: `GET /inventory` exposes package, port, camera, calibration, and
  optional sim smoke status without motor commands.
- Phase 4: `GET /operations/templates`, `POST /operations/request`, `POST /stop`,
  and real-rollout preflight block risky workflows by default.
- Phase 5: `GET /datasets` returns dataset summary with explicit upload.
- Phase 6: `GET /policies/compatibility` blocks real rollout when mapping is
  unknown or remote-code trust is not granted.
- Phase 7: `GET /agent/tools` exposes diagnostic/sim tools and disabled physical
  tools with scoped permissions.
- Phase 8: `GET /packaging/plan` records Tauri preferred with Electron fallback
  and `POST /support-bundle/export` excludes secrets.

## Consequences

The repo now has a complete roadmap skeleton that can be verified without
hardware. Next work should deepen one track: isolated SDK smoke, read-only
adapter implementation, desktop packaging spike, or UI runtime tests.

## Related

- `../../roadmap/phases.json`
- `../../apps/desktop/README.md`
- `../../services/local-gateway/README.md`
- `../../tools/verify_phase.py`
