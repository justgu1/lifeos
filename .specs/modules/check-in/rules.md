# RULES

## REQUIRED

- RULE-001: DailyBlocks are materialized deterministically from the routine for that weekday
- RULE-002: DailyBlock completion is idempotent
- RULE-003: points are snapshotted from default_points at materialization and immutable to later catalog edits
- RULE-004: Sunday is free and materializes no DailyBlocks
- RULE-005: one Day exists per date and belongs to the active Week
- RULE-006: a block_id must resolve to a BlockDefinition

## SECURITY

- single-user scope, no auth
- reject completing another day's block
- validate all input at the boundary

## PERFORMANCE

- GET /today is a single indexed projection read (hot path)
- materialization is lazy on first open

## OBSERVABILITY

- log check completions with day id + block id + trace-id
- emit streak metric

## EXCEPTIONS

| rule | exception |
|----------|----------|
| RULE-004 | none |
| RULE-002 | re-completion returns success without state change |
