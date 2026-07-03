"""Event-type registry and handler dispatch.

Domain modules register handlers here; the platform never imports domain modules.
Known event types are seeded from the shared contract constants.
"""

from __future__ import annotations

import json
from collections import defaultdict
from collections.abc import Callable
from pathlib import Path
from typing import Any

from sqlalchemy.orm import Session

Handler = Callable[[Session, "DispatchedEvent"], None]


class DispatchedEvent:
    """The persisted event handed to registered handlers."""

    def __init__(self, id: str, aggregate_id: str, aggregate_type: str, version: int,
                 event_type: str, payload: dict[str, Any], created_at: str,
                 schema_version: int = 1) -> None:
        self.id = id
        self.aggregate_id = aggregate_id
        self.aggregate_type = aggregate_type
        self.version = version
        self.event_type = event_type
        self.schema_version = schema_version
        self.payload = payload
        self.created_at = created_at


def _load_known_event_types() -> set[str]:
    # packages/shared/schema/constants.json is the single source of truth.
    root = Path(__file__).resolve().parents[5]
    constants = root / "packages" / "shared" / "schema" / "constants.json"
    try:
        data = json.loads(constants.read_text(encoding="utf-8"))
        return set(data.get("eventTypes", {}).values())
    except FileNotFoundError:
        return set()


class EventHandlerRegistry:
    def __init__(self) -> None:
        self._handlers: dict[str, list[Handler]] = defaultdict(list)
        self._known: set[str] = _load_known_event_types()

    def register_type(self, event_type: str) -> None:
        self._known.add(event_type)

    def is_known(self, event_type: str) -> bool:
        return event_type in self._known

    def on(self, event_type: str, handler: Handler) -> None:
        self._known.add(event_type)
        self._handlers[event_type].append(handler)

    def dispatch(self, session: Session, event: DispatchedEvent) -> None:
        for handler in self._handlers.get(event.event_type, []):
            handler(session, event)


registry = EventHandlerRegistry()
