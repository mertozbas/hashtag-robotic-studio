# Hashtag Robotic Studio Memory

This folder contains local searchable memory for Hashtag Robotic Studio.

Install:

```bash
python3 -m venv .memory/.venv
.memory/.venv/bin/pip install -r .memory/requirements.txt
```

Seed memory:

```bash
.memory/.venv/bin/python .memory/ingest_all.py
```

Query memory:

```bash
.memory/.venv/bin/python .memory/query.py "agent robot control safety gate" --top-k 5
.memory/.venv/bin/python .memory/query.py "Strands Robots 0.4.1" --type sdk_decision --status active
```

Add a new memory source:

```bash
.memory/.venv/bin/python .memory/ingest.py product_decision "Short title" memory/source/decisions/file.md --area product --tags so101,studio
```

The vector database is stored under `.memory/chroma` and is intentionally ignored by git.

