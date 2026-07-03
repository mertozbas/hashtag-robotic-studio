# Hashtag Robotic Studio

Hashtag Robotic Studio is the planning and Codex workspace for the SO101 customer desktop application.

The product goal is a local-first desktop studio that ships with Hashtag Robotics SO101 robots. A customer should connect the SO101 follower arm, optional leader arm, and cameras to a PC, open the app, and manage setup, calibration checks, teleoperation, data recording, dataset review, policy validation, and agent-driven robot operation without using a terminal.

This folder is intentionally product-private for now. It contains product design, architecture, safety rules, local memory, and Codex operating instructions. The shippable app can later live in the same repo or be split out once implementation begins.

Start here:

- [docs/PRODUCT_SPEC.md](docs/PRODUCT_SPEC.md)
- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)
- [docs/SAFETY_MODEL.md](docs/SAFETY_MODEL.md)
- [docs/AGENT_ROBOT_CONTROL_MODEL.md](docs/AGENT_ROBOT_CONTROL_MODEL.md)
- [docs/UI_UX_SYSTEM.md](docs/UI_UX_SYSTEM.md)
- [docs/REFERENCE_INDEX.md](docs/REFERENCE_INDEX.md)

Codex workflow:

```bash
.memory/.venv/bin/python .memory/query.py "SO101 Studio safety gate" --top-k 5
python3 tools/next_task.py
python3 tools/context_pack.py --phase phase-1 --task "local gateway skeleton"
```

If the memory environment is not installed yet:

```bash
python3 -m venv .memory/.venv
.memory/.venv/bin/pip install -r .memory/requirements.txt
.memory/.venv/bin/python .memory/ingest_all.py
```

Autonomous development system:

- [.codex/config.toml](.codex/config.toml): project-local Codex autonomy defaults.
- [.codex/agents/](.codex/agents): specialist subagents for product, UX, backend, safety, SDK, QA, and memory.
- [roadmap/phases.json](roadmap/phases.json): machine-readable phase plan.
- [knowledge/](knowledge/00-index/README.md): local markdown vault for low-token project memory.
- [docs/AUTONOMOUS_CODEX_WORKFLOW.md](docs/AUTONOMOUS_CODEX_WORKFLOW.md): one-input implementation loop.
- [docs/EXPERT_AGENT_SYSTEM.md](docs/EXPERT_AGENT_SYSTEM.md): specialist agent roles.
- [docs/TOKEN_EFFICIENCY.md](docs/TOKEN_EFFICIENCY.md): context and token budget rules.
