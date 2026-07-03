"""Event store: append, load, optimistic concurrency, dispatch (PLATFORM-002)."""

from app.infrastructure.event_store.errors import ConcurrencyError, UnknownEventTypeError
from app.infrastructure.event_store.registry import EventHandlerRegistry, registry
from app.infrastructure.event_store.store import EventStore, NewEvent

__all__ = [
    "ConcurrencyError",
    "EventHandlerRegistry",
    "EventStore",
    "NewEvent",
    "UnknownEventTypeError",
    "registry",
]
