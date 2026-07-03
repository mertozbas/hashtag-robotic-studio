# Parallel Review Template

Use when a phase implementation is ready for review.

```text
Review the current branch with parallel subagents. Spawn one agent per role and wait for all of them:
1. robot-safety-reviewer: physical safety, calibration, rollout, destructive operations.
2. test-qa-engineer: missing tests, flaky tests, contract coverage.
3. ux-designer: UI clarity, Turkish/English i18n, cockpit usability.
4. local-gateway-architect: backend contracts, event streams, state machines.

Return a consolidated finding list ordered by severity with file references.
Do not implement changes until the findings are summarized.
```

