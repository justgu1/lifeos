"""Application configuration loaded from the environment (see .env.example)."""

from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Settings:
    database_url: str
    timezone: str
    notification_hours: tuple[int, ...]
    week_start_day: str
    cycle_length_weeks: int

    @classmethod
    def from_env(cls) -> Settings:
        hours_raw = os.getenv("LIFEOS_NOTIFICATION_HOURS", "13,18,22")
        hours = tuple(int(h) for h in hours_raw.split(",") if h.strip())
        return cls(
            database_url=os.getenv("LIFEOS_DATABASE_URL", "sqlite:///./lifeos.db"),
            timezone=os.getenv("LIFEOS_TIMEZONE", "America/Sao_Paulo"),
            notification_hours=hours,
            week_start_day=os.getenv("LIFEOS_WEEK_START_DAY", "monday"),
            cycle_length_weeks=int(os.getenv("LIFEOS_CYCLE_LENGTH_WEEKS", "13")),
        )


def get_settings() -> Settings:
    return Settings.from_env()
