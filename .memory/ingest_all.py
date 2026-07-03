from __future__ import annotations

import argparse
import json
from pathlib import Path

from common import DEFAULT_PROJECT, ROOT, fail, ingest_file, split_tags

DEFAULT_MANIFEST = ROOT / ".memory" / "seed_manifest.json"


def main() -> None:
    parser = argparse.ArgumentParser(description="Ingest all configured Hashtag Robotic Studio memory sources.")
    parser.add_argument("--manifest", default=str(DEFAULT_MANIFEST))
    args = parser.parse_args()

    manifest_path = Path(args.manifest)
    if not manifest_path.exists():
        fail(f"Manifest not found: {manifest_path}")

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    items = manifest.get("items", [])
    if not items:
        fail(f"No items found in manifest: {manifest_path}")

    total_chunks = 0
    for item in items:
        source = ROOT / item["file"]
        count, prefix = ingest_file(
            memory_type=item["type"],
            title=item["title"],
            file_path=source,
            status=item.get("status", "active"),
            area=item.get("area", "general"),
            importance=item.get("importance", "medium"),
            tags=split_tags(",".join(item.get("tags", []))),
            project=item.get("project", DEFAULT_PROJECT),
            chunk_size=item.get("chunk_size", 5000),
            chunk_overlap=item.get("chunk_overlap", 500),
        )
        total_chunks += count
        print(f"{prefix}: {count} chunk{'s' if count != 1 else ''} from {item['file']}")

    print(f"Ingest complete: {len(items)} sources, {total_chunks} chunks.")


if __name__ == "__main__":
    main()
