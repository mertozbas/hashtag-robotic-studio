# Autonomous Codex Workflow

Last updated: 2026-07-04

This document defines how Codex should work on Hashtag Robotic Studio with minimal repeated prompting.

## Goal

Turn one user input into a complete work loop:

1. load focused context
2. pick the next phase task
3. implement
4. test
5. update docs/knowledge/memory
6. commit
7. recommend the next task

This system is for building Hashtag Robotic Studio. It is not part of the customer-facing app runtime.

## Default Autonomy

Project-local config sets:

- `approval_policy = "never"`
- `sandbox_mode = "danger-full-access"`
- `model_verbosity = "low"`
- `web_search = "cached"`
- `features.goals = true`
- `features.memories = true`
- `features.multi_agent = true`

Codex should not ask routine implementation questions. It should make conservative decisions from project docs and existing patterns.

## Hard Stops

Even in autonomous mode, Codex must stop before:

- physical robot movement
- teleoperation
- real policy rollout
- calibration overwrite
- dataset/checkpoint deletion
- long training jobs
- model downloads
- Docker pulls
- external account/login/payment actions
- public publishing

## Recommended Commands

Get next task:

```bash
python3 tools/next_task.py
```

Generate focused context:

```bash
python3 tools/context_pack.py --phase phase-1 --task "local gateway skeleton"
```

Verify phase:

```bash
python3 tools/verify_phase.py --phase phase-1
```

Use Goal mode:

```text
/goal
Run Phase 1 from roadmap/phases.json. Use tools/context_pack.py first, implement, test, update docs/memory, commit, and report the next task. No physical robot movement.
```

## Token Efficiency Rules

- Keep `AGENTS.md` durable and short.
- Put long details in `docs/`, `knowledge/`, and `memory/source/`.
- Use `.memory/query.py` and `tools/context_pack.py` instead of reading everything.
- Prefer summaries from subagents, not raw logs.
- Use web search only when facts may have changed.
- Use `web_search = "cached"` by default.
- Use targeted file reads and `rg`, not broad dumps.
- Update memory after decisions so future turns retrieve compact facts.

## Multi-agent Use

Use subagents for parallel read-heavy work:

- product architecture review
- UX review
- safety review
- test review
- SDK surface exploration

Avoid parallel write-heavy work unless the files are clearly separated.

