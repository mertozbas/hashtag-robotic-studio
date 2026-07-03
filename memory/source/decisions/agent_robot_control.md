# Agent Robot Control Decision

Status: active

The Strands agent is allowed to operate the SO101 robot. This is a product differentiator.

The agent must not bypass deterministic product safety.

Required model:

1. User gives a goal.
2. Strands Agent reasons and selects tools.
3. Tool creates or requests a typed `RobotOperation`.
4. `SafetyGate` checks operation requirements.
5. User unlock is required for physical motion unless a short-lived explicit permission scope is active.
6. Deterministic runner enforces limits, stop behavior, and logging.
7. LeRobot or Strands Robots talks to hardware.

The agent can diagnose, simulate, plan, request physical operations, and control within approved bounded sessions. It cannot silently choose ports, overwrite calibration, ignore feature mapping blockers, or send unbounded motion.

