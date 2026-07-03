# Version Plan

Last updated: 2026-07-04

## Version Semantics

- `v0.0.x`: Codex workspace, docs, contracts, non-actuating prototypes.
- `v0.1.x`: Local gateway and desktop cockpit prototype.
- `v0.2.x`: Read-only SO101 integration.
- `v0.3.x`: Controlled physical workflows.
- `v0.4.x`: Dataset Studio.
- `v0.5.x`: Policy Studio.
- `v0.6.x`: Agent-driven robot operation.
- `v0.7.x`: Packaging and customer install beta.
- `v1.0.0`: Customer-ready SO101 Studio release.

## Current Version

`v0.0.1`: product workspace and autonomous Codex development system.

## Release Gates

No release with physical robot motion can be tagged unless:

- SafetyGate tests pass
- emergency stop behavior is verified with fake/sim runner
- no physical movement path can start without user unlock
- calibration overwrite path requires backup and explicit confirmation
- support bundle masks secrets

