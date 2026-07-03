# Phase Goal Template

Use this with `/goal` from the project root.

```text
Implement Phase <N> of Hashtag Robotic Studio from roadmap/phases.json.

Constraints:
- Work autonomously without asking follow-up questions unless physical hardware movement, calibration overwrite, dataset/checkpoint deletion, long training, model download, or external account action is required.
- Use docs/PRODUCT_SPEC.md, docs/ARCHITECTURE.md, docs/SAFETY_MODEL.md, docs/AGENT_ROBOT_CONTROL_MODEL.md, docs/UI_UX_SYSTEM.md, docs/SDK_STRATEGY.md, and the relevant context pack.
- Keep the implementation scoped to this phase.
- Add or update tests/checks.
- Run verification.
- Update docs, knowledge, and memory when decisions change.
- Commit the completed phase.

Definition of done:
- Phase acceptance criteria pass.
- No physical robot movement occurred unless explicitly authorized.
- Git status contains only intentional changes.
- The final message reports changed files, tests run, and next recommended phase.
```

