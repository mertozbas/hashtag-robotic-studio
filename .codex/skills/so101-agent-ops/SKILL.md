# SO101 Agent Operations Skill

Use this skill when designing or implementing Strands Agent features for Hashtag Robotic Studio.

## Required Reads

Read before acting:

- `docs/AGENT_ROBOT_CONTROL_MODEL.md`
- `docs/SAFETY_MODEL.md`
- `docs/ARCHITECTURE.md`
- `docs/SDK_STRATEGY.md`

Query memory:

```bash
.memory/.venv/bin/python .memory/query.py "Strands agent robot operation tools SafetyGate" --top-k 5
```

## Agent Rules

- The agent may operate the robot. That is the product feature.
- The agent operates through tools, not raw driver access.
- Physical tools are session-scoped and expire.
- Diagnostic and simulation tools are available before physical tools.
- Physical operation requests must pass SafetyGate and user unlock.
- Tool-call stream should be visible in the Agent cockpit.

## Tool Design Pattern

Prefer tools shaped like:

```text
diagnose_* -> no motion
simulate_* -> no real motion
prepare_* -> no motion
request_*_operation -> creates RobotOperation
run_*_session_action -> only available inside approved session
stop_operation -> always available
```

