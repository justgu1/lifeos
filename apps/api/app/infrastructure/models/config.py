"""Singleton application config row."""

from __future__ import annotations

from sqlalchemy import JSON, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.db.base import Base


class ConfigRow(Base):
    __tablename__ = "config"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, default=1)
    timezone: Mapped[str] = mapped_column(String(64), nullable=False)
    notification_hours: Mapped[list] = mapped_column(JSON, nullable=False)
    week_start_day: Mapped[str] = mapped_column(String(16), nullable=False, default="monday")
    cycle_length_weeks: Mapped[int] = mapped_column(Integer, nullable=False, default=13)
    flags: Mapped[dict] = mapped_column(JSON, nullable=False, default=dict)
