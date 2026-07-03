# Token Efficiency Strategy

Last updated: 2026-07-04

## Principle

Codex should spend tokens on decisions and implementation, not rediscovering project context.

## System Components

- `AGENTS.md`: short durable rules.
- `docs/`: canonical product and architecture documents.
- `knowledge/`: Obsidian-like local markdown vault.
- `memory/source/`: compact durable facts for vector retrieval.
- `.memory/query.py`: semantic retrieval.
- `tools/context_pack.py`: focused context assembly.
- `roadmap/phases.json`: machine-readable phase/task plan.
- `.codex/agents/`: specialist subagents.

## Workflow

1. Query memory.
2. Generate context pack.
3. Read only referenced files.
4. Implement.
5. Verify.
6. Summarize decision changes.
7. Update memory and knowledge.

## What Not To Do

- Do not paste all docs into every prompt.
- Do not make `AGENTS.md` huge.
- Do not use live web for stable local facts.
- Do not spawn many subagents for simple edits.
- Do not keep raw logs in the main thread when a summary is enough.

