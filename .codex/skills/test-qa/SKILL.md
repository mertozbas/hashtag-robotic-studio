# Test QA Skill

Use this skill when writing tests, verification scripts, acceptance checks, or reviewing implementation quality.

## Required Reads

- `docs/IMPLEMENTATION_ROADMAP.md`
- `docs/SAFETY_MODEL.md`
- `roadmap/phases.json`

## Rules

- Prefer tests that run without hardware first.
- SafetyGate and operation state machine tests are mandatory before physical workflows.
- UI tests should cover blocked/ready/running/stopped states.
- SDK integration tests should have fake/sim paths before real hardware paths.

## Default Check

```bash
python3 tools/verify_phase.py --phase <phase-id>
```

