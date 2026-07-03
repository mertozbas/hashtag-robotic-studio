from __future__ import annotations

import argparse
from collections import Counter

from common import get_collection


def main() -> None:
    parser = argparse.ArgumentParser(description="Inspect memory health before manual compaction.")
    parser.add_argument("--limit", type=int, default=500)
    args = parser.parse_args()

    collection = get_collection()
    count = collection.count()
    if count == 0:
        print("Project memory is empty.")
        return

    results = collection.get(limit=min(args.limit, count), include=["metadatas"])
    metadatas = results.get("metadatas", [])

    by_type = Counter(meta.get("type", "unknown") for meta in metadatas)
    by_status = Counter(meta.get("status", "unknown") for meta in metadatas)
    by_area = Counter(meta.get("area", "unknown") for meta in metadatas)

    print(f"Memory chunks: {count}")
    print("\nBy type:")
    for key, value in by_type.most_common():
        print(f"  {key}: {value}")

    print("\nBy status:")
    for key, value in by_status.most_common():
        print(f"  {key}: {value}")

    print("\nBy area:")
    for key, value in by_area.most_common():
        print(f"  {key}: {value}")

    print("\nCompaction rule:")
    print("  Every 20-30 sessions, merge repeated session summaries into canonical active decisions,")
    print("  mark old conflicting notes as superseded/deprecated, and keep docs/PROJECT_STATE.md short.")


if __name__ == "__main__":
    main()
