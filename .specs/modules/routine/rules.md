# RULES

## REQUIRED

- RULE-001: a DailyBlock always traces to a BlockDefinition
- RULE-002: deactivating a block must not delete history
- RULE-003: points come from default_points
- RULE-004: blocks are scheduled Monday..Saturday only (Sunday is free)

## SECURITY

- single-user scope, no auth
- validate emoji/color/category at boundary

## PERFORMANCE

- catalog cached
- routine lookup by weekday indexed

## OBSERVABILITY

- log routine version changes

## EXCEPTIONS

| rule | exception |
|----------|----------|
| RULE-004 | Sunday remains free and holds no scheduled blocks |
