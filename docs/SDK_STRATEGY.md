# SDK Strategy

Last updated: 2026-07-04

## Decision

Target `strands-robots==0.4.1` for Hashtag Robotic Studio, while preserving the rule that active lab environments are upgraded only after isolated smoke tests.

## Why Not Stay On 0.4.0?

The parent SO101 lab currently uses `strands-robots==0.4.0` because that was the stable installed baseline when the lab environment was created.

For a new product workspace, use the newest verified release path. `0.4.1` is especially relevant because the public release notes emphasize sim/real parity, policy/simulation flow, state-key mismatch handling, episode validation, and output path safety. Those are product-critical areas.

## Upgrade Strategy

Do not upgrade a working environment blindly.

Use a separate environment:

```bash
python3.12 -m venv .venv-strands-041
.venv-strands-041/bin/pip install -U pip
.venv-strands-041/bin/pip install "strands-robots[sim-mujoco,lerobot]==0.4.1"
```

Smoke tests:

1. import `strands_robots`
2. inspect installed providers
3. create `Robot("so101", mode="sim", mesh=False)`
4. call `reset()`
5. inspect observation keys
6. inspect action/state dimensions
7. check SO101 real construction path without motion only when explicitly approved
8. check teleop surface
9. check recording surface
10. run existing ACT dry-run if available

## Dependency Rules

- Avoid `all` extras until each family has a concrete purpose.
- Install policy families one at a time.
- Treat mesh, IoT, device-connect, ROS, MoveIt2, cuRobo, GR00T, Cosmos, Newton, and benchmark packages as separate integration tracks.
- Keep LeRobot compatibility visible in the UI.
- Remote code trust must be explicit.

## Product Capability Detection

The app should not assume package features.

At startup, create a capability inventory:

- installed package versions
- installed Strands providers
- installed extras
- LeRobot import status
- camera backend status
- policy providers
- simulation backend status
- recording support
- teleoperation support

Display missing capabilities as product blockers, not Python tracebacks.

## Parent Lab Compatibility

The parent `/Users/macmert/so101-test` lab remains useful for evidence and experiments. Do not patch LeRobot or the parent lab environment from this product workspace unless explicitly requested.

