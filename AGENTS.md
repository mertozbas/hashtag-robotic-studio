# Hashtag Robotic Studio Codex Operating Guide

This file is loaded by Codex when working from `/Users/macmert/so101-test/hashtag-robotic-studio`.

## Project Identity

- Product: `Hashtag Robotic Studio`, customer-facing desktop software for Hashtag Robotics SO101 robots.
- Primary robot: RobotStudio SO101 follower arm plus optional SO101 leader arm.
- Product category: local-first robot setup, control, data collection, dataset review, policy validation, and agent-driven robot operation studio.
- UI language: Turkish by default with English support.
- Core stack direction: desktop shell plus local Python gateway, Strands Agents, Strands Robots, LeRobot, WebSocket event streams, local persistent config, and explicit safety gates.
- Product stance: Coolify and self-hosted PaaS are out of scope. Policy download, dataset upload, support bundle export, and account/auth integrations should happen directly inside the app when needed.

## Before Non-trivial Work

1. Read:
   - `docs/PROJECT_STATE.md`
   - `docs/CURRENT_SPRINT.md`
   - `docs/PRODUCT_SPEC.md`
   - `docs/SAFETY_MODEL.md` when touching robot control, agent tools, or real hardware paths.
2. Query project memory with a task-specific query:

   ```bash
   .memory/.venv/bin/python .memory/query.py "<task query>" --top-k 5
   ```

3. Prefer `status=active` memories. Treat `deprecated`, `superseded`, and `rejected` memories as historical only.
4. If memory conflicts, follow this order:
   - `docs/CURRENT_SPRINT.md`
   - `docs/PROJECT_STATE.md`
   - `docs/SAFETY_MODEL.md`
   - active `safety_rule` memories
   - active `architecture_decision` memories
   - active `product_decision` memories
   - latest `session_summary` memories
   - older design notes

Do not dump the whole memory store into context. Use targeted retrieval.

## Product Rules

- The app must be local-first. Core robot workflows must work without a cloud server.
- Agent-driven robot operation is a flagship feature, not an afterthought.
- The agent may operate the robot only through explicit tools and operation contracts. It must not bypass deterministic safety gates, motion limits, calibration requirements, or logging.
- LeRobot remains the source of truth for SO101 driver behavior, calibration semantics, dataset schema, and proven record/train/eval workflows.
- Strands Robots is the orchestration layer for `Robot()`, simulation, policy abstraction, robot tools, mesh/ROS experiments, and agent-facing capabilities.
- Prefer target SDK `strands-robots==0.4.1`, but verify in an isolated environment before upgrading any working lab environment.
- The UI must expose capability detection instead of assuming an SDK feature exists.

## Hardware Safety Rules

- Do not send motor commands, run teleoperation, run rollout, calibrate, replay actions, or start autonomous policy execution unless the user explicitly asks for that physical action in the current turn.
- Before any physical actuation, confirm command path, follower port, leader port if used, camera config, calibration id, selected policy/checkpoint if any, expected duration/step limit, workspace clearance, and emergency stop path.
- Prefer observation-only inventory, simulation, and dry-run checks before actuation.
- Never assume `/dev/tty*`, `/dev/cu*`, COM ports, or camera indices. Discover and report candidates first.
- Do not overwrite calibration files unless explicitly requested.
- Do not delete datasets, checkpoints, logs, calibration files, or caches unless explicitly requested.
- Long installs, full SDK extras, Docker pulls, model downloads, training jobs, Hub pushes, and real hardware tests require explicit approval.
- Never expose secrets. If a token or credential is found, mention only the file/location and remediation.

## Development Rules

- Use `rg` or `rg --files` before slower search commands.
- Make manual edits with `apply_patch`.
- Preserve user changes. Do not revert unrelated files.
- Keep changes scoped to product docs, app code, robot adapters, contracts, local gateway, UI, memory, or Codex workflow.
- Prefer existing Strands/LeRobot APIs over custom wrappers unless a wrapper captures a repeated product workflow or safety contract.
- Put risky operations behind explicit contracts and testable state machines.
- Add focused tests or validation steps when changes affect contracts, safety, adapter behavior, or user-facing flows.

## UI Rules

- Build a serious glass cockpit, not a decorative glassmorphism page.
- Use glass effects for chrome, HUD, and status panels; use solid high-contrast surfaces for logs, tables, warnings, and destructive or physical actions.
- Critical controls such as emergency stop, motor lock, calibration write, and real rollout must be visually unambiguous and never hidden behind decorative styling.
- Turkish strings are first-class. English must be available through i18n dictionaries, not hard-coded branches.
- Keep robot workflows dense, scannable, and operational. Avoid marketing sections inside the app.

## Memory Maintenance

After a meaningful session, add memory when one of these changed:

- product decision
- architecture decision
- safety rule
- SDK decision
- UI decision
- agent operation rule
- hardware profile or calibration note
- dataset decision
- policy decision
- implementation note
- bug fix or failure mode
- rejected idea
- open question
- session summary

Example:

```bash
.memory/.venv/bin/python .memory/ingest.py product_decision "Local-first product stance" memory/source/decisions/local_first_product.md --area product --tags local-first,desktop,so101 --importance critical
```

Keep `docs/PROJECT_STATE.md` and `docs/CURRENT_SPRINT.md` short. Long details belong in `memory/source` and the vector DB.

