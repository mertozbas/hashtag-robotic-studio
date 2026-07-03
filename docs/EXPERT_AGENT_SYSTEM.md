# Expert Agent System

Last updated: 2026-07-04

This project defines specialized Codex subagents under `.codex/agents/`.

Codex spawns them only when explicitly asked. They are for reducing main-thread context noise and improving review quality.

## Agents

| Agent | Purpose |
| --- | --- |
| `product-architect` | Product scope, phase planning, tradeoffs, contract needs. |
| `ux-designer` | Turkish-first glass cockpit UX and usability. |
| `frontend-engineer` | Desktop UI implementation. |
| `local-gateway-architect` | FastAPI gateway, contracts, event streams, state machines. |
| `sdk-integration-engineer` | Strands Robots, LeRobot, camera, dataset, policy integrations. |
| `agent-ops-architect` | Strands Agent robot tools and operation scopes. |
| `robot-safety-reviewer` | Physical safety, calibration, rollout, destructive operation review. |
| `test-qa-engineer` | Contract tests, fake/sim tests, UI tests, packaging smoke tests. |
| `docs-memory-curator` | Vault, memory, docs, roadmap, token efficiency. |

## Usage Patterns

Architecture planning:

```text
Spawn product-architect, local-gateway-architect, and robot-safety-reviewer. Ask each to review Phase 1 and return blockers plus implementation order.
```

UI design review:

```text
Spawn ux-designer and frontend-engineer to review the current UI plan. Wait for both, then consolidate.
```

Safety review:

```text
Spawn robot-safety-reviewer for a read-only review of the current branch. Lead with blockers.
```

Phase review:

```text
Use .codex/prompts/parallel-review-template.md.
```

## Cost Control

- Use subagents for bounded reviews, not every small task.
- Ask for summaries, not full transcripts.
- Prefer one agent per independent concern.
- Keep `agents.max_depth = 1` to avoid recursive fan-out.

