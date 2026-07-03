---
module: platform

version: 0.1.0

depends_on: []

skills:
---

# PURPOSE

Own the event-sourcing infrastructure: the append-only event store, snapshots, the transactional outbox, application Config, and offline sync. It is the only module aware of SQLAlchemy/SQLite and the single write path (POST /events). It routes events to owning modules through a handler registry and never imports domain modules.

# SCOPE

includes:
- Events table (append-only) with optimistic concurrency
- Snapshots (latest-only per aggregate) and rebuild-from-snapshot+tail
- transactional Outbox and its relay/drain
- Config singleton
- SyncService (offline outbox push/pull and reconciliation)
- event-handler registry and dispatch
- POST /events ingestion
- event serialization and schema versioning (upcasters)

excludes:
- any business rule or invariant of a specific aggregate
- read-model shapes owned by domain/review modules (platform only stores/dispatches)

# FLOWS

## FLOW-001

actor: client or domain service
trigger: POST /events with a batch for an aggregate
result: events persisted, dispatched to registered handlers, outbox rows queued

steps:
- validate request against the generated shared schema
- deduplicate by event id (idempotent)
- rehydrate aggregate (latest snapshot + tail replay)
- let the owning handler validate invariants
- in one transaction: insert events (version = expected_version + i), insert outbox rows, update projections
- on UNIQUE(aggregate_id, version) violation return 409

## FLOW-002

actor: SyncService
trigger: connectivity restored or scheduled interval
result: pending outbox delivered and reconciled

steps:
- read outbox rows where status = pending ordered by created_at
- deliver (device to server, or server to downstream)
- mark sent with synced_at, or failed incrementing attempts
- on server, reconcile 409 conflicts by re-reading current version

## FLOW-003

actor: snapshot scheduler
trigger: weekly cadence or version - snapshot.version >= N
result: aggregate snapshot written and SnapshotCreated emitted

steps:
- select aggregates needing a snapshot
- rebuild latest state
- upsert latest-only snapshot
- emit SnapshotCreated

# ENTITIES

## EventRecord

append-only fact; unique (aggregate_id, version) and unique id.

## Snapshot

latest-only per aggregate.

## OutboxItem

transactional delivery queue item.

## Config

singleton application configuration.
