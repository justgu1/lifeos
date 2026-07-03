# CHECKLISTS

implementation:
- payload-validation
- ordered-atomic-emission
- config-init
- contracts-respected
- rules-respected

tests:
- partial-failure-rollback
- idempotency
- resulting-first-week-is-active
- unit-tests
- integration-tests

artifacts:
- synchronized

delivery:
- one-work-item-one-pr
- ci-green (unit + e2e + apk-build)
- changelog-updated
