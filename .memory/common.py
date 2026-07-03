from __future__ import annotations

import hashlib
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DB_PATH = ROOT / ".memory" / "chroma"
COLLECTION = "hashtag_robotic_studio_memory"
DEFAULT_PROJECT = "hashtag_robotic_studio"


def require_chromadb():
    try:
        import chromadb  # type: ignore
    except ImportError as exc:
        message = (
            "chromadb is not installed. Run:\n"
            "  python3 -m venv .memory/.venv\n"
            "  .memory/.venv/bin/pip install -r .memory/requirements.txt"
        )
        raise SystemExit(message) from exc
    return chromadb


def get_collection():
    chromadb = require_chromadb()
    DB_PATH.mkdir(parents=True, exist_ok=True)
    client = chromadb.PersistentClient(path=str(DB_PATH))
    return client.get_or_create_collection(COLLECTION)


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def relative_source(path: Path) -> str:
    resolved = path.resolve()
    try:
        return str(resolved.relative_to(ROOT))
    except ValueError:
        return str(resolved)


def split_tags(raw: str | None) -> str:
    if not raw:
        return ""
    tags = [tag.strip() for tag in raw.split(",") if tag.strip()]
    return ",".join(dict.fromkeys(tags))


def chunk_text(text: str, max_chars: int = 5000, overlap: int = 500) -> list[str]:
    cleaned = text.strip()
    if not cleaned:
        return []
    if len(cleaned) <= max_chars:
        return [cleaned]

    chunks: list[str] = []
    start = 0
    length = len(cleaned)
    while start < length:
        end = min(start + max_chars, length)
        if end < length:
            paragraph_break = cleaned.rfind("\n\n", start, end)
            line_break = cleaned.rfind("\n", start, end)
            cut = paragraph_break if paragraph_break > start + max_chars // 2 else line_break
            if cut > start + max_chars // 2:
                end = cut
        chunk = cleaned[start:end].strip()
        if chunk:
            chunks.append(chunk)
        if end >= length:
            break
        start = max(0, end - overlap)
    return chunks


def build_where(filters: dict[str, str | None]) -> dict[str, Any] | None:
    conditions: list[dict[str, str]] = []
    for key, value in filters.items():
        if value:
            conditions.append({key: value})
    if not conditions:
        return None
    if len(conditions) == 1:
        return conditions[0]
    return {"$and": conditions}


def stable_prefix(memory_type: str, title: str, source_file: str) -> str:
    digest = hashlib.sha1(f"{memory_type}|{title}|{source_file}".encode("utf-8")).hexdigest()[:12]
    safe_type = "".join(ch if ch.isalnum() else "_" for ch in memory_type.lower()).strip("_")
    return f"{safe_type}_{digest}"


def ingest_file(
    *,
    memory_type: str,
    title: str,
    file_path: Path,
    status: str = "active",
    area: str = "general",
    importance: str = "medium",
    tags: str = "",
    project: str = DEFAULT_PROJECT,
    chunk_size: int = 5000,
    chunk_overlap: int = 500,
) -> tuple[int, str]:
    if not file_path.exists():
        raise FileNotFoundError(file_path)

    content = file_path.read_text(encoding="utf-8")
    chunks = chunk_text(content, max_chars=chunk_size, overlap=chunk_overlap)
    if not chunks:
        raise ValueError(f"No text content found in {file_path}")

    source = relative_source(file_path)
    prefix = stable_prefix(memory_type, title, source)
    collection = get_collection()

    delete_where = build_where({
        "type": memory_type,
        "title": title,
        "source_file": source,
    })
    if delete_where:
        try:
            collection.delete(where=delete_where)
        except Exception:
            pass

    created_at = utc_now()
    ids = [f"{prefix}_{index:03d}" for index in range(len(chunks))]
    metadatas = []
    for index, chunk in enumerate(chunks):
        metadatas.append({
            "project": project,
            "type": memory_type,
            "title": title,
            "status": status,
            "area": area,
            "importance": importance,
            "tags": tags,
            "source_file": source,
            "created_at": created_at,
            "chunk_index": index,
            "chunk_total": len(chunks),
            "content_chars": len(chunk),
        })

    collection.add(ids=ids, documents=chunks, metadatas=metadatas)
    return len(chunks), prefix


def fail(message: str) -> None:
    print(message, file=sys.stderr)
    raise SystemExit(1)
