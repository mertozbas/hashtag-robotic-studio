# Codex CLI Workflow

Last updated: 2026-07-04

## Start Of Session

From `hashtag-robotic-studio/`:

```bash
sed -n '1,220p' docs/PROJECT_STATE.md
sed -n '1,220p' docs/CURRENT_SPRINT.md
.memory/.venv/bin/python .memory/query.py "<task query>" --top-k 5
python3 tools/next_task.py
```

If memory is not installed:

```bash
python3 -m venv .memory/.venv
.memory/.venv/bin/pip install -r .memory/requirements.txt
.memory/.venv/bin/python .memory/ingest_all.py
```

## Before Robot-related Changes

Read:

- `docs/SAFETY_MODEL.md`
- `docs/AGENT_ROBOT_CONTROL_MODEL.md`
- `docs/SDK_STRATEGY.md`

Then query memory:

```bash
.memory/.venv/bin/python .memory/query.py "physical motion safety gate SO101 agent operation" --top-k 5
```

## Before UI Changes

Read:

- `docs/UI_UX_SYSTEM.md`
- `docs/PRODUCT_SPEC.md`

Then query memory:

```bash
.memory/.venv/bin/python .memory/query.py "glass cockpit UI SO101 Studio Turkish English" --top-k 5
```

## Before SDK Changes

Read:

- `docs/SDK_STRATEGY.md`
- `docs/REFERENCE_INDEX.md`

Then query memory:

```bash
.memory/.venv/bin/python .memory/query.py "Strands Robots 0.4.1 upgrade strategy SO101" --top-k 5
```

## Memory Maintenance

Add source file under `memory/source/...`, then ingest:

```bash
.memory/.venv/bin/python .memory/ingest.py architecture_decision "Short title" memory/source/decisions/file.md --area architecture --tags so101,studio --importance high
```

Update `.memory/seed_manifest.json` if the memory is foundational.

## Autonomous Phase Work

For a long implementation run:

```text
/goal
Run the next phase from roadmap/phases.json. Use tools/context_pack.py first, implement, test, update docs/knowledge/memory, commit, and report the next task. No physical robot movement.
```

Useful commands:

```bash
python3 tools/next_task.py
python3 tools/context_pack.py --phase phase-1 --task "local gateway skeleton"
python3 tools/verify_phase.py --phase phase-1
```

Use `.codex/prompts/phase-autopilot.md` for a reusable prompt.

## Git Rules

- Keep product-private docs and Codex system in this repo.
- Do not commit local virtualenvs, Chroma DB, datasets, checkpoints, logs, videos, support bundles, or secrets.
- Commit focused changes.
