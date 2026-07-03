---
item: event-store-snapshot-outbox
module: platform
status: active
priority: high
depends_on: [PLATFORM-001, SHARED-001]
---

# CHANGE

Implement the event store (append-only Events, optimistic concurrency), snapshots (latest-only + rebuild-from-snapshot+tail), the transactional outbox with relay, the Config singleton, the handler registry, and the POST /events ingestion endpoint.

## WHY

This is the system of record (ADR-001) and the single write path (ADR-004) that every domain module depends on.

## SCOPE

### Included

- SQLAlchemy models + Alembic migrations for events, snapshots, outbox, config
- append with UNIQUE(aggregate_id, version) optimistic concurrency
- idempotent ingestion by event id
- snapshot write + rebuild (snapshot + tail replay)
- transactional outbox + relay/drain
- handler registry + dispatch
- POST /events endpoint validating against the shared schema
- SQLite WAL configuration

### Excluded

- any specific aggregate's invariants (owned by domain modules)
- offline device sync (PLATFORM-003)

## ACCEPTANCE

### AC-001

Given two concurrent appends at the same expected_version

When both are submitted

Then exactly one succeeds and the other returns HTTP 409.

### AC-002

Given a duplicated event id

When re-ingested

Then it is accepted idempotently (not an error) and stored once.

### AC-003

Given an aggregate with a snapshot and later events

When rebuilt

Then the state equals full replay from zero.

## NOTES

Follows platform contracts (domain/api/events) exactly.
