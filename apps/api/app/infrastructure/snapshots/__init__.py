"""Snapshot writer/reader and rebuild-from-snapshot+tail (PLATFORM-002)."""

from app.infrastructure.snapshots.store import SnapshotStore

__all__ = ["SnapshotStore"]
