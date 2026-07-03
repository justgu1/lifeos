# CHECKLISTS

implementation:
- projection-builders-per-period
- review-orchestration
- contracts-respected
- rules-respected

tests:
- unit-tests
- integration-tests
- projection-equals-replay-parity
- already-reviewed-rejection

artifacts:
- synchronized

delivery:
- one-work-item-one-pr
- ci-green (unit + e2e + apk-build)
- changelog-updated
