from __future__ import annotations

import pytest

from app.infrastructure.event_store import ConcurrencyError, EventStore
from app.infrastructure.event_store.store import NewEvent
from app.infrastructure.models import EventRecord, OutboxItem
from app.infrastructure.snapshots import SnapshotStore


def _ev(n: int) -> NewEvent:
    return NewEvent(event_type="test.happened", payload={"n": n})


def test_append_assigns_contiguous_versions(session) -> None:
    store = EventStore()
    dispatched = store.append(session, "agg-1", "test", 0, [_ev(1), _ev(2)])
    assert [d.version for d in dispatched] == [1, 2]
    assert store.current_version(session, "agg-1") == 2


def test_optimistic_concurrency_conflict(session) -> None:
    store = EventStore()
    store.append(session, "agg-1", "test", 0, [_ev(1)])
    with pytest.raises(ConcurrencyError):
        store.append(session, "agg-1", "test", 0, [_ev(2)])  # stale expected_version


def test_idempotent_reingest(session) -> None:
    store = EventStore()
    e = NewEvent(event_type="test.happened", payload={"n": 1}, id="EVENT01")
    store.append(session, "agg-1", "test", 0, [e])
    # Re-ingest same id: no new events, no error.
    again = store.append(session, "agg-1", "test", 0, [e])
    assert again == []
    count = session.query(EventRecord).filter_by(aggregate_id="agg-1").count()
    assert count == 1


def test_outbox_written_in_same_transaction(session) -> None:
    store = EventStore()
    store.append(session, "agg-1", "test", 0, [_ev(1), _ev(2)])
    outbox = session.query(OutboxItem).all()
    assert len(outbox) == 2
    assert all(o.status == "pending" for o in outbox)
    assert outbox[0].payload["aggregate_id"] == "agg-1"


def test_snapshot_plus_tail_equals_full_replay(session) -> None:
    store = EventStore()
    snaps = SnapshotStore(store)
    for i in range(1, 11):
        store.append(session, "agg-1", "test", i - 1, [_ev(i)])

    full = sum(e.payload["n"] for e in store.load_events(session, "agg-1"))

    # Snapshot at version 6 with the folded state so far.
    snaps.save(session, "agg-1", "test", 6, {"sum": sum(range(1, 7))})
    snap, tail = snaps.load_for_rebuild(session, "agg-1")
    assert snap is not None
    rebuilt = snap.payload["sum"] + sum(e.payload["n"] for e in tail)
    assert rebuilt == full
    assert [e.version for e in tail] == [7, 8, 9, 10]
