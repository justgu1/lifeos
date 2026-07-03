"""Outbox relay — drains pending rows with at-least-once delivery."""

from __future__ import annotations

from collections.abc import Callable
from datetime import UTC, datetime

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.infrastructure.models import OutboxItem, OutboxStatus

Deliver = Callable[[dict], None]


def _now() -> str:
    return datetime.now(UTC).isoformat()


class OutboxRelay:
    def pending(self, session: Session, limit: int = 100) -> list[OutboxItem]:
        return list(
            session.execute(
                select(OutboxItem)
                .where(OutboxItem.status == OutboxStatus.PENDING.value)
                .order_by(OutboxItem.created_at)
                .limit(limit)
            ).scalars()
        )

    def drain(self, session: Session, deliver: Deliver, limit: int = 100) -> int:
        """Deliver pending rows. Returns the number successfully delivered."""
        delivered = 0
        for item in self.pending(session, limit):
            try:
                deliver(item.payload)
                item.status = OutboxStatus.SENT.value
                item.synced_at = _now()
                delivered += 1
            except Exception as exc:  # noqa: BLE001 - record and continue
                item.attempts += 1
                item.last_error = str(exc)[:500]
                item.status = OutboxStatus.FAILED.value
        session.commit()
        return delivered
