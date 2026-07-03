"""Event store domain-ish errors mapped to HTTP by the presentation layer."""

from __future__ import annotations


class ConcurrencyError(Exception):
    """Raised when expected_version does not match the aggregate's current version."""

    def __init__(self, aggregate_id: str, expected: int, actual: int) -> None:
        self.aggregate_id = aggregate_id
        self.expected = expected
        self.actual = actual
        super().__init__(
            f"version conflict on {aggregate_id}: expected {expected}, actual {actual}"
        )


class UnknownEventTypeError(Exception):
    """Raised when an event_type is not registered."""

    def __init__(self, event_type: str) -> None:
        self.event_type = event_type
        super().__init__(f"unknown event_type: {event_type}")
