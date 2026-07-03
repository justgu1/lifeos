# CHECKLISTS

implementation:
- schedule
- dispatch
- suppress-when-complete
- contracts-respected
- rules-respected

tests:
- unit-tests
- integration-tests
- timezone-correctness
- suppression-when-complete

artifacts:
- synchronized

delivery:
- one-work-item-one-pr
- ci-green (unit + e2e + apk-build)
- changelog-updated
