"""ULID generation — time-sortable ids for events and outbox rows."""

from __future__ import annotations

from ulid import ULID


def new_ulid() -> str:
    return str(ULID())
