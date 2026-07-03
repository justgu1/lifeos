"""Append-only event store table."""

from __future__ import annotations

from datetime import UTC, datetime

from sqlalchemy import JSON, Index, Integer, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.db.base import Base


class EventRecord(Base):
    __tablename__ = "events"
    __table_args__ = (
        UniqueConstraint("aggregate_id", "version", name="uq_events_aggregate_version"),
        Index("ix_events_aggregate", "aggregate_id", "version"),
        Index("ix_events_type_created", "aggregate_type", "created_at"),
    )

    id: Mapped[str] = mapped_column(String(26), primary_key=True)  # ULID
    aggregate_id: Mapped[str] = mapped_column(String(36), nullable=False)
    aggregate_type: Mapped[str] = mapped_column(String(64), nullable=False)
    version: Mapped[int] = mapped_column(Integer, nullable=False)
    event_type: Mapped[str] = mapped_column(String(64), nullable=False)
    schema_version: Mapped[int] = mapped_column(Integer, nullable=False, default=1)
    payload: Mapped[dict] = mapped_column(JSON, nullable=False)
    created_at: Mapped[str] = mapped_column(String(32), nullable=False)

    @staticmethod
    def now_iso() -> str:
        return datetime.now(UTC).isoformat()
