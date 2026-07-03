# CHECKLISTS

implementation:
- materialization
- completion
- idempotency
- today-projection
- contracts-respected
- rules-respected

tests:
- unit-tests
- integration-tests
- timezone-day-boundary
- offline-replay-ordering

artifacts:
- synchronized

delivery:
- one-work-item-one-pr
- ci-green (unit + e2e + apk-build)
- changelog-updated
