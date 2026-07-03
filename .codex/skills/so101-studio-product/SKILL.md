---
name: so101-studio-product
description: Use when designing or implementing Hashtag Robotic Studio product surfaces, customer workflows, dashboard scope, product architecture, Turkish/English UX, or feature tradeoffs.
---

# SO101 Studio Product Skill

Use this skill when designing or implementing product surfaces for Hashtag Robotic Studio.

## Required Reads

Read before acting:

- `docs/PRODUCT_SPEC.md`
- `docs/UI_UX_SYSTEM.md`
- `docs/ARCHITECTURE.md`
- `docs/CURRENT_SPRINT.md`

Query memory:

```bash
.memory/.venv/bin/python .memory/query.py "SO101 Studio product UI architecture" --top-k 5
```

## Product Rules

- Turkish first, English selectable.
- Build the actual robot studio experience, not a marketing landing page.
- Keep UI independent from backend SDK changes by using contracts.
- Do not add cloud infrastructure unless the current task proves a specific need.
- Keep customer mode simple, lab mode powerful, developer mode transparent.

## Useful Output

For design tasks, produce:

- screen purpose
- primary controls
- state model
- blockers/errors
- API/contract requirements
- safety implications
