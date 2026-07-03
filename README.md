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
```

If the memory environment is not installed yet:

```bash
python3 -m venv .memory/.venv
.memory/.venv/bin/pip install -r .memory/requirements.txt
.memory/.venv/bin/python .memory/ingest_all.py
```

