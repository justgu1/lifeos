"""Outbox writer and relay/dispatcher (PLATFORM-002 / PLATFORM-003)."""

from app.infrastructure.outbox.relay import OutboxRelay

__all__ = ["OutboxRelay"]
