# Reference Index

Last updated: 2026-07-04

Use this file to quickly find the external and local references behind the product direction.

## Strands Robots

- GitHub: https://github.com/strands-labs/robots
- Releases: https://github.com/strands-labs/robots/releases
- PyPI: https://pypi.org/project/strands-robots/
- Abstraction Cartography: https://cagataycali.github.io/abstraction-cartography/

Why it matters:

- robot orchestration layer
- `Robot()` abstraction
- simulation path
- policy providers
- agent-facing robot tools
- future mesh/ROS/device-connect direction

Current product decision:

- target `strands-robots==0.4.1` for new product work
- verify installed surface before relying on any provider or extra
- keep `mode="sim"` and `mesh=False` as default safe smoke path

## Strands Agents

- Main docs: https://strandsagents.com
- Robots Sim docs: https://strandsagents.com/docs/labs/robots-sim/

Why it matters:

- agent runtime
- tool-call orchestration
- streaming interaction model
- natural language robot control workflows

Current product decision:

- agent is a first-class robot operator
- agent must operate through explicit tools, operation contracts, and SafetyGate

## Scout The Rover

- Repo: https://github.com/cagataycali/scout-the-rover

Why it matters:

- useful reference for a robot dashboard that is more than UI
- glass cockpit direction
- FastAPI gateway pattern
- WebSocket agent streaming
- camera/telemetry/control proxy
- passkey/auth and e-stop awareness

Current product decision:

- borrow the local gateway plus cockpit pattern
- adapt it for SO101 manipulator safety, calibration, dataset, and policy workflows

## LeRobot

- GitHub: https://github.com/huggingface/lerobot
- SO101 docs: https://huggingface.co/docs/lerobot/en/so101

Why it matters:

- SO101 driver source of truth
- calibration semantics
- leader/follower workflows
- LeRobotDataset format
- baseline policy training/evaluation

Current product decision:

- LeRobot compatibility is mandatory
- app should wrap LeRobot workflows instead of replacing them

## SO101 Context

- NVIDIA SO101 learning path: https://docs.nvidia.com/learning/physical-ai/sim-to-real-so-101/latest/04-lerobot.html
- NVIDIA calibration guide: https://docs.nvidia.com/learning/physical-ai/sim-to-real-so-101/latest/07-calibrating-so101.html
- Phospho SO101 quickstart reference: https://docs.phospho.ai/so-101/quickstart

Why it matters:

- confirms the leader/follower mental model
- reinforces calibration as a physical safety and accuracy step
- gives competitive/product inspiration for customer onboarding

## Parent Lab References

From `/Users/macmert/so101-test`:

- `../docs/PROJECT_STATE.md`
- `../docs/CURRENT_SPRINT.md`
- `../docs/STRANDS_ROBOTS_OPERATING_MODEL.md`
- `../docs/SO101_FEATURE_MAPPING.md`
- `../docs/ROBOT_PREFLIGHT_CHECKLIST.md`
- `../docs/DASHBOARD_MVP_PLAN.md`
- `../docs/ABSTRACTION_CARTOGRAPHY_STRANDS_ROBOTS_REVIEW.md`
- `../docs/ABSTRACTION_CARTOGRAPHY_STRANDS_ROBOTS_REVIEW_TR.md`

Why it matters:

- current lab evidence
- installed package reality
- SO101 calibration/dataset facts
- safety gates
- feature mapping risks

