from __future__ import annotations

import json
from collections import deque
from collections.abc import Iterable

from packages.contracts import OperationEvent


class EventStore:
    def __init__(self, maxlen: int = 200) -> None:
        self._events: deque[OperationEvent] = deque(maxlen=maxlen)

    def append(self, event: OperationEvent) -> OperationEvent:
        self._events.append(event)
        return event

    def list(self, limit: int = 50) -> list[OperationEvent]:
        if limit <= 0:
            return []
        return list(self._events)[-limit:]

    def as_sse(self, limit: int = 50) -> Iterable[str]:
        for event in self.list(limit=limit):
            payload = event.model_dump(mode="json")
            yield f"event: {event.type}\ndata: {json.dumps(payload, separators=(',', ':'))}\n\n"
