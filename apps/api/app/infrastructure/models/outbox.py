"""Transactional outbox — written in the same transaction as the events."""

from __future__ import annotations

import enum

from sqlalchemy import JSON, Index, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.db.base import Base


class OutboxStatus(enum.StrEnum):
    PENDING = "pending"
    SENT = "sent"
    FAILED = "failed"


class OutboxItem(Base):
    __tablename__ = "outbox"
    __table_args__ = (Index("ix_outbox_status", "status"),)

    id: Mapped[str] = mapped_column(String(26), primary_key=True)  # ULID
    payload: Mapped[dict] = mapped_column(JSON, nullable=False)
    status: Mapped[str] = mapped_column(
        String(16), nullable=False, default=OutboxStatus.PENDING.value
    )
    attempts: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    last_error: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[str] = mapped_column(String(32), nullable=False)
    synced_at: Mapped[str | None] = mapped_column(String(32), nullable=True)
