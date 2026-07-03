# Hashtag Robotic Studio Safety Model

Status: active

Every physical robot operation must pass through:

- typed operation contract
- SafetyGate preflight
- explicit user unlock when physical motion is involved
- deterministic runner
- duration and action limits
- emergency stop path
- event logging

Block real rollout if any of these are unknown:

- follower port
- camera config
- calibration id
- selected policy or agent tool plan
- image key mapping
- state/action feature order
- action dimension
- unit conversion
- gripper range/direction
- duration or step limit
- emergency stop path

The app may run observation, inventory, diagnostics, and simulation without physical motion. It must not assume ports or move hardware automatically.

