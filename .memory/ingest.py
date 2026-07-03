from __future__ import annotations

import argparse
from pathlib import Path

from common import DEFAULT_PROJECT, ingest_file, split_tags


def main() -> None:
    parser = argparse.ArgumentParser(description="Add or refresh a Hashtag Robotic Studio memory source file.")
    parser.add_argument("type", help="Memory type, e.g. product_decision or architecture_decision.")
    parser.add_argument("title", help="Human-readable memory title.")
    parser.add_argument("file_path", help="Markdown/text source file to ingest.")
    parser.add_argument("--status", default="active")
    parser.add_argument("--area", default="general")
    parser.add_argument("--importance", default="medium")
    parser.add_argument("--tags", default="")
    parser.add_argument("--project", default=DEFAULT_PROJECT)
    parser.add_argument("--chunk-size", type=int, default=5000)
    parser.add_argument("--chunk-overlap", type=int, default=500)
    args = parser.parse_args()

    count, prefix = ingest_file(
        memory_type=args.type,
        title=args.title,
        file_path=Path(args.file_path),
        status=args.status,
        area=args.area,
        importance=args.importance,
        tags=split_tags(args.tags),
        project=args.project,
        chunk_size=args.chunk_size,
        chunk_overlap=args.chunk_overlap,
    )
    print(f"Added memory: {prefix} ({count} chunk{'s' if count != 1 else ''})")


if __name__ == "__main__":
    main()
