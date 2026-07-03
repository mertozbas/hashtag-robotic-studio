---
name: autonomous-workflow
description: Use when Codex should continue work, run the next roadmap phase, work autonomously, reduce repeated prompts, or complete a multi-step implementation loop with context packing, verification, memory updates, and commits for Hashtag Robotic Studio.
---

# Autonomous Workflow Skill

Use this skill when the user asks Codex to continue work, run the next phase, work autonomously, reduce repeated prompts, or complete a multi-step implementation loop.

## Required Reads

- `docs/AUTONOMOUS_CODEX_WORKFLOW.md`
- `roadmap/phases.json`
- `docs/CURRENT_SPRINT.md`
- `docs/PROJECT_STATE.md`

## Required Commands

```bash
python3 tools/next_task.py
python3 tools/context_pack.py --phase <phase-id> --task "<task>"
```

## Workflow

1. Identify the phase/task.
2. Generate focused context.
3. Implement.
4. Run relevant tests and `python3 tools/verify_phase.py --phase <phase-id>`.
5. Update docs, knowledge, and memory when durable facts changed.
6. Commit intentional changes.
7. Report next task.

## Hard Stops

Stop and ask only for physical robot movement, calibration overwrite, dataset/checkpoint deletion, long training/model download, Docker pull, external login/account action, or public publishing.
