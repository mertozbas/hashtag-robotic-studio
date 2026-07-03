# Strands Robots 0.4.1 Target Strategy

Status: active

Target `strands-robots==0.4.1` for Hashtag Robotic Studio.

The parent SO101 lab currently uses `strands-robots==0.4.0`; do not mutate that working environment without explicit approval.

Upgrade path:

1. Create an isolated Python 3.12 environment.
2. Install `strands-robots[sim-mujoco,lerobot]==0.4.1`.
3. Run import and provider discovery.
4. Run `Robot("so101", mode="sim", mesh=False)` smoke test.
5. Inspect observation/action/state keys.
6. Verify teleop and recording surfaces.
7. Only then decide whether to update active lab or product dependencies.

The app must use capability detection rather than assuming every cartography feature exists in the installed package.

