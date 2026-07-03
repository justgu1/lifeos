# RULES

## REQUIRED

- RULE-001: events are append-only; never updated or deleted
- RULE-002: optimistic concurrency enforced by UNIQUE(aggregate_id, version); version is 1-based and contiguous per aggregate
- RULE-003: ingestion is idempotent by event id (duplicate id is accepted, not an error)
- RULE-004: outbox rows are written in the same transaction as the events (transactional outbox)
- RULE-005: event_type must be registered in the handler registry to be accepted
- RULE-006: reads are served from projections; the aggregate rebuild path is snapshot + tail replay
- RULE-007: schema_version on each event enables upcasting at load time; stored events are never rewritten
- RULE-008: platform must not import domain modules; domain modules register handlers/ports into platform

## SECURITY

- validate and whitelist event_type against the registry
- never store secrets in event payloads
- validate input at the POST /events boundary

## PERFORMANCE

- index UNIQUE(aggregate_id, version) and a temporal ordering index (ULID id)
- batch inserts for event and outbox writes
- snapshots bound replay cost
- SQLite runs in WAL mode with busy_timeout so the relay coexists with writes

## OBSERVABILITY

- trace-id per ingestion batch
- structured log per dispatched handler
- outbox-lag and snapshot metrics

## EXCEPTIONS

| rule | exception |
|----------|----------|
| RULE-003 | a duplicate event id returns accepted (idempotent replay), not a validation error |
| RULE-002 | version conflict returns HTTP 409 for client-side reconciliation |
