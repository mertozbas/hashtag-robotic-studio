# SO101 Robot Safety Skill

Use this skill when touching physical robot operations, calibration, teleoperation, real rollout, agent tools that can move hardware, or destructive dataset/checkpoint actions.

## Required Reads

Read before acting:

- `docs/SAFETY_MODEL.md`
- `docs/AGENT_ROBOT_CONTROL_MODEL.md`
- `docs/ARCHITECTURE.md`

Query memory:

```bash
.memory/.venv/bin/python .memory/query.py "SO101 safety physical motion SafetyGate" --top-k 5
```

## Hard Rules

- Do not move hardware unless the user explicitly requested physical actuation in the current turn.
- Do not assume ports or camera indices.
- Do not overwrite calibration files without explicit request.
- Do not let an agent bypass SafetyGate.
- Unknown policy mapping blocks real rollout.
- All physical operations need timeout, stop path, logging, and user unlock.

## Review Checklist

For any physical operation path, verify:

- operation type
- requester
- selected mode
- follower port
- leader port when relevant
- camera config
- calibration id
- policy/checkpoint if relevant
- feature mapping if relevant
- duration/step limit
- speed/action limit
- emergency stop
- event logging

