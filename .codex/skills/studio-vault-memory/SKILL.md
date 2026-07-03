---
name: studio-vault-memory
description: Use when creating or updating Hashtag Robotic Studio project knowledge, markdown vault notes, memory sources, seed manifests, worklogs, or token-efficient context workflows.
---

# Studio Vault And Memory Skill

Use this skill when creating or updating project knowledge, memory, decisions, worklogs, or token-efficient context.

## Required Reads

- `knowledge/00-index/README.md`
- `.memory/README.md`
- `docs/TOKEN_EFFICIENCY.md`
- `docs/CODEX_CLI_WORKFLOW.md`

## Workflow

1. Put detailed notes in `knowledge/`.
2. Put durable searchable facts in `memory/source/`.
3. Update `.memory/seed_manifest.json` only for foundational memories.
4. Run `.memory/.venv/bin/python .memory/ingest_all.py` after manifest changes.
5. Keep `AGENTS.md` short.

## Note Types

Use `docs/templates/vault-note-template.md`.
