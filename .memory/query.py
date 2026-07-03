from __future__ import annotations

import argparse
import json
from typing import Any

from common import build_where, get_collection


def main() -> None:
    parser = argparse.ArgumentParser(description="Search Hashtag Robotic Studio memory.")
    parser.add_argument("query")
    parser.add_argument("--top-k", type=int, default=5)
    parser.add_argument("--type", default=None)
    parser.add_argument("--status", default=None)
    parser.add_argument("--area", default=None)
    parser.add_argument("--importance", default=None)
    parser.add_argument("--max-chars", type=int, default=2200)
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of readable text.")
    args = parser.parse_args()

    collection = get_collection()
    count = collection.count()
    if count == 0:
        print("Project memory is empty. Run `.memory/.venv/bin/python .memory/ingest_all.py` first.")
        return

    where = build_where({
        "type": args.type,
        "status": args.status,
        "area": args.area,
        "importance": args.importance,
    })

    results = collection.query(
        query_texts=[args.query],
        n_results=min(max(args.top_k, 1), count),
        where=where,
    )

    docs = results.get("documents", [[]])[0]
    metas = results.get("metadatas", [[]])[0]
    distances = results.get("distances", [[]])[0]

    rows: list[dict[str, Any]] = []
    for index, doc in enumerate(docs):
        meta = metas[index] if index < len(metas) else {}
        distance = distances[index] if index < len(distances) else None
        rows.append({
            "rank": index + 1,
            "distance": distance,
            "metadata": meta,
            "content": doc,
        })

    if args.json:
        print(json.dumps(rows, ensure_ascii=False, indent=2))
        return

    for row in rows:
        meta = row["metadata"]
        content = row["content"]
        if len(content) > args.max_chars:
            content = content[: args.max_chars].rstrip() + "\n..."

        print("=" * 88)
        print(f"Rank: {row['rank']} | Distance: {row['distance']}")
        print(f"Title: {meta.get('title')}")
        print(f"Type: {meta.get('type')} | Status: {meta.get('status')} | Area: {meta.get('area')}")
        print(f"Importance: {meta.get('importance')} | Tags: {meta.get('tags')}")
        print(f"Source: {meta.get('source_file')} | Chunk: {meta.get('chunk_index')}/{meta.get('chunk_total')}")
        print("-" * 88)
        print(content)
        print()


if __name__ == "__main__":
    main()
