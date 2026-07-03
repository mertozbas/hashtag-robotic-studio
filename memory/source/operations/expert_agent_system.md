# Expert Agent System

Status: active

Specialized Codex subagents are configured under `.codex/agents/`:

- product-architect
- ux-designer
- frontend-engineer
- local-gateway-architect
- sdk-integration-engineer
- agent-ops-architect
- robot-safety-reviewer
- test-qa-engineer
- docs-memory-curator

Use subagents for broad or parallel read-heavy work such as architecture review, safety review, UI review, SDK exploration, and test-gap analysis. Avoid unnecessary subagents for small edits because each subagent consumes extra tokens.

Subagents inherit parent sandbox/approval settings unless overridden. The robot-safety-reviewer is read-only.

