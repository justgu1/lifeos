# CHECKLISTS

implementation:
- append-load-replay-implemented
- optimistic-concurrency-implemented
- snapshot-write-and-rebuild-implemented
- transactional-outbox-and-relay-implemented
- idempotent-ingestion-implemented
- handler-registry-and-dispatch-implemented
- config-singleton-implemented
- contracts-respected
- rules-respected

tests:
- unit-tests
- integration-tests
- replay-determinism-tested
- idempotent-reingest-tested
- version-conflict-409-tested
- alembic-migration-up-down-tested

artifacts:
- synchronized
- openapi-for-post-events

delivery:
- one-work-item-one-pr
- ci-green (unit + e2e + apk-build)
- changelog-updated
