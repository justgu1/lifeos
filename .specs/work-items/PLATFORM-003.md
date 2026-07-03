---
item: offline-outbox-sync
module: platform
status: draft
priority: medium
depends_on: [PLATFORM-002, CHECKIN-001]
---

# CHANGE

Implement offline-first: a local SQLite event log and outbox on the device, and the SyncService that pushes pending events to POST /events and reconciles conflicts, then pulls fresh projections.

## WHY

The daily check-in must work without internet (ADR-004); events are captured locally and synced later.

## SCOPE

### Included

- device-side local SQLite event log + outbox (apps/web lib/offline)
- SyncService push/pull with idempotent replay and 409 reconciliation
- conflict handling and retry with attempts/last_error
- tests for offline replay ordering and idempotency

### Excluded

- notifications (NOTIF-001)

## ACCEPTANCE

### AC-001

Given events recorded offline

When connectivity returns

Then the outbox drains to POST /events idempotently and projections refresh.

### AC-002

Given a version conflict on sync

When reconciling

Then the client re-reads the current version and resolves without data loss.

## NOTES

Delivery is at-least-once; ingestion dedupes by event id.
