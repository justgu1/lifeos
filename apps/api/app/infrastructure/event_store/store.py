"""Append-only event store with optimistic concurrency and transactional outbox."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime

from sqlalchemy import func, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.infrastructure.event_store.errors import ConcurrencyError
from app.infrastructure.event_store.ids import new_ulid
from app.infrastructure.event_store.registry import DispatchedEvent, EventHandlerRegistry, registry
from app.infrastructure.models import EventRecord, OutboxItem


def _now() -> str:
    return datetime.now(UTC).isoformat()


@dataclass(slots=True)
class NewEvent:
    event_type: str
    payload: dict
    id: str | None = None
    schema_version: int = 1
    created_at: str = field(default_factory=_now)


class EventStore:
    def __init__(self, handler_registry: EventHandlerRegistry | None = None) -> None:
        self._registry = handler_registry or registry

    def current_version(self, session: Session, aggregate_id: str) -> int:
        result = session.execute(
            select(func.max(EventRecord.version)).where(EventRecord.aggregate_id == aggregate_id)
        ).scalar_one_or_none()
        return int(result or 0)

    def load_events(
        self, session: Session, aggregate_id: str, after_version: int = 0
    ) -> list[EventRecord]:
        return list(
            session.execute(
                select(EventRecord)
                .where(
                    EventRecord.aggregate_id == aggregate_id,
                    EventRecord.version > after_version,
                )
                .order_by(EventRecord.version)
            ).scalars()
        )

    def append(
        self,
        session: Session,
        aggregate_id: str,
        aggregate_type: str,
        expected_version: int,
        events: list[NewEvent],
    ) -> list[DispatchedEvent]:
        """Append events atomically (events + outbox in one transaction).

        Idempotent by event id; raises ConcurrencyError on version mismatch.
        Returns the newly appended events (already-known ids are skipped).
        """
        ids = [e.id for e in events if e.id]
        existing: set[str] = set()
        if ids:
            existing = set(
                session.execute(
                    select(EventRecord.id).where(EventRecord.id.in_(ids))
                ).scalars()
            )
        new_events = [e for e in events if not (e.id and e.id in existing)]
        if not new_events:
            return []  # fully idempotent replay

        current = self.current_version(session, aggregate_id)
        if current != expected_version:
            raise ConcurrencyError(aggregate_id, expected_version, current)

        dispatched: list[DispatchedEvent] = []
        for offset, ev in enumerate(new_events, start=1):
            version = expected_version + offset
            event_id = ev.id or new_ulid()
            record = EventRecord(
                id=event_id,
                aggregate_id=aggregate_id,
                aggregate_type=aggregate_type,
                version=version,
                event_type=ev.event_type,
                schema_version=ev.schema_version,
                payload=ev.payload,
                created_at=ev.created_at,
            )
            session.add(record)
            envelope = {
                "id": event_id,
                "aggregate_id": aggregate_id,
                "aggregate_type": aggregate_type,
                "version": version,
                "event_type": ev.event_type,
                "schema_version": ev.schema_version,
                "payload": ev.payload,
                "created_at": ev.created_at,
            }
            session.add(OutboxItem(id=new_ulid(), payload=envelope, created_at=_now()))
            dispatched.append(DispatchedEvent(**envelope))

        try:
            session.flush()
        except IntegrityError as exc:
            session.rollback()
            raise ConcurrencyError(
                aggregate_id, expected_version, self.current_version(session, aggregate_id)
            ) from exc

        for event in dispatched:
            self._registry.dispatch(session, event)

        session.commit()
        return dispatched
