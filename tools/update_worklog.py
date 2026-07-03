#!/usr/bin/env python3
from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    parser = argparse.ArgumentParser(description="Append a lightweight worklog entry to the Studio vault.")
    parser.add_argument("title")
    parser.add_argument("--phase", default="")
    parser.add_argument("--summary", default="")
    args = parser.parse_args()

    today = datetime.now().strftime("%Y-%m-%d")
    slug = "".join(ch.lower() if ch.isalnum() else "-" for ch in args.title).strip("-")
    path = ROOT / "knowledge/worklogs" / f"{today}-{slug}.md"
    content = [
        "---",
        f'title: "{args.title}"',
        "type: worklog",
        "status: active",
        f'area: "{args.phase or "general"}"',
        "tags: [worklog]",
        f"created: {today}",
        f"updated: {today}",
        "---",
        "",
        f"# {args.title}",
        "",
        "## Summary",
        "",
        args.summary or "-",
        "",
        "## Verification",
        "",
        "-",
        "",
        "## Follow-up",
        "",
        "-",
        "",
    ]
    path.write_text("\n".join(content), encoding="utf-8")
    print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()

