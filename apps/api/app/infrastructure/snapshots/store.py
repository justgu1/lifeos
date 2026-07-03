"""Latest-only snapshots. Read path = snapshot + tail replay."""

from __future__ import annotations

from datetime import UTC, datetime

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.infrastructure.event_store.store import EventStore
from app.infrastructure.models import EventRecord, Snapshot


def _now() -> str:
    return datetime.now(UTC).isoformat()


class SnapshotStore:
    def __init__(self, event_store: EventStore | None = None) -> None:
        self._events = event_store or EventStore()

    def get(self, session: Session, aggregate_id: str) -> Snapshot | None:
        return session.get(Snapshot, aggregate_id)

    def save(
        self,
        session: Session,
        aggregate_id: str,
        aggregate_type: str,
        version: int,
        payload: dict,
    ) -> Snapshot:
        snap = session.get(Snapshot, aggregate_id)
        if snap is None:
            snap = Snapshot(
                aggregate_id=aggregate_id,
                aggregate_type=aggregate_type,
                version=version,
                payload=payload,
                created_at=_now(),
            )
            session.add(snap)
        else:
            snap.aggregate_type = aggregate_type
            snap.version = version
            snap.payload = payload
            snap.created_at = _now()
        session.commit()
        return snap

    def load_for_rebuild(
        self, session: Session, aggregate_id: str
    ) -> tuple[Snapshot | None, list[EventRecord]]:
        """Return the latest snapshot (if any) and the tail of events after it."""
        snap = self.get(session, aggregate_id)
        base_version = snap.version if snap else 0
        tail = self._events.load_events(session, aggregate_id, after_version=base_version)
        return snap, tail

    def all_tail_events(self, session: Session, aggregate_id: str) -> list[EventRecord]:
        return list(
            session.execute(
                select(EventRecord)
                .where(EventRecord.aggregate_id == aggregate_id)
                .order_by(EventRecord.version)
            ).scalars()
        )
