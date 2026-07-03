# Hashtag Robotic Studio Vault

This is a local markdown vault inspired by Obsidian-style knowledge organization.

It is plain files, not a dependency on Obsidian.

Purpose:

- keep product decisions searchable
- reduce repeated context in Codex sessions
- preserve implementation knowledge
- give future agents structured context

## Folders

- `decisions/`: durable choices and rejected paths
- `specs/`: product and feature specs
- `architecture/`: contracts, adapters, runtime notes
- `safety/`: physical robot safety and preflight notes
- `ui/`: screen notes, i18n, interaction patterns
- `agent/`: Strands agent tool and permission designs
- `backend/`: local gateway, API, event stream notes
- `testing/`: test plans, acceptance criteria, QA notes
- `research/`: external source summaries and current-source checks
- `worklogs/`: session summaries and phase implementation logs

## Note Template

Use `docs/templates/vault-note-template.md`.

## Rules

- One note should capture one decision, feature, risk, or implementation area.
- Add YAML frontmatter for type/status/tags.
- Keep notes linked with relative markdown links when useful.
- Move durable facts into `memory/source/` when they should be retrievable by Codex.

