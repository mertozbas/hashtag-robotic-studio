# Studio Vault And Token Strategy

Status: active

The project uses a plain markdown vault under `knowledge/` instead of depending on Obsidian.

Purpose:

- preserve structured product knowledge
- reduce repeated context in Codex prompts
- keep AGENTS.md compact
- store detailed notes outside the main instruction chain
- promote durable facts into `memory/source/` for semantic retrieval

Token efficiency pattern:

1. Query `.memory`.
2. Generate a focused context pack with `tools/context_pack.py`.
3. Read only the files referenced by the task.
4. Update docs/vault/memory after decisions.
5. Use subagents only for bounded reviews or parallel exploration.

