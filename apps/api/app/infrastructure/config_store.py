"""Config singleton accessor."""

from __future__ import annotations

from sqlalchemy.orm import Session

from app.infrastructure.models import ConfigRow

CONFIG_ID = 1


def get_config(session: Session) -> ConfigRow | None:
    return session.get(ConfigRow, CONFIG_ID)


def upsert_config(
    session: Session,
    *,
    timezone: str,
    notification_hours: list[int],
    week_start_day: str = "monday",
    cycle_length_weeks: int = 13,
    flags: dict | None = None,
) -> ConfigRow:
    row = session.get(ConfigRow, CONFIG_ID)
    if row is None:
        row = ConfigRow(id=CONFIG_ID)
        session.add(row)
    row.timezone = timezone
    row.notification_hours = notification_hours
    row.week_start_day = week_start_day
    row.cycle_length_weeks = cycle_length_weeks
    row.flags = flags or {}
    session.commit()
    return row
