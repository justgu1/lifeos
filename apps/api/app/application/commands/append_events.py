"""Append-events command — the single write path behind POST /events."""

from __future__ import annotations

from dataclasses import dataclass, field

from pydantic import ValidationError
from sqlalchemy.orm import Session

from app.application.event_models import validate_payload
from app.infrastructure.event_store import ConcurrencyError, EventStore, UnknownEventTypeError
from app.infrastructure.event_store.registry import registry
from app.infrastructure.event_store.store import NewEvent


@dataclass(slots=True)
class IncomingEvent:
    id: str
    aggregate_id: str
    aggregate_type: str
    expected_version: int
    event_type: str
    payload: dict
    schema_version: int = 1
    created_at: str | None = None


@dataclass(slots=True)
class AppendResult:
    accepted: list[str] = field(default_factory=list)
    conflicts: list[dict] = field(default_factory=list)


class AppendEventsCommand:
    def __init__(self, store: EventStore | None = None) -> None:
        self._store = store or EventStore()

    def execute(self, session: Session, events: list[IncomingEvent]) -> AppendResult:
        result = AppendResult()

        # Validate first (fail the batch on malformed/unknown events).
        for ev in events:
            if not registry.is_known(ev.event_type):
                raise UnknownEventTypeError(ev.event_type)
            try:
                validate_payload(ev.event_type, ev.payload)
            except ValidationError as exc:
                raise ValueError(f"invalid payload for {ev.event_type}: {exc}") from exc

        # Group by aggregate, preserving order.
        groups: dict[str, list[IncomingEvent]] = {}
        for ev in events:
            groups.setdefault(ev.aggregate_id, []).append(ev)

        for aggregate_id, group in groups.items():
            expected = group[0].expected_version
            new_events = []
            for ev in group:
                kwargs = {
                    "event_type": ev.event_type,
                    "payload": ev.payload,
                    "id": ev.id,
                    "schema_version": ev.schema_version,
                }
                if ev.created_at:
                    kwargs["created_at"] = ev.created_at
                new_events.append(NewEvent(**kwargs))
            try:
                dispatched = self._store.append(
                    session, aggregate_id, group[0].aggregate_type, expected, new_events
                )
                if dispatched:
                    result.accepted.extend(d.id for d in dispatched)
                else:
                    # Idempotent replay — all ids already stored.
                    result.accepted.extend(ev.id for ev in group)
            except ConcurrencyError as exc:
                for ev in group:
                    result.conflicts.append(
                        {"id": ev.id, "reason": "VERSION_CONFLICT",
                         "expected": exc.expected, "actual": exc.actual}
                    )
        return result
