# RULES

## REQUIRED

- RULE-001: a Goal belongs to exactly one Vision
- RULE-002: Goal progress is derived and never set directly
- RULE-003: GoalService owns Goal creation
- RULE-004: only one active Vision exists at a time

## SECURITY

- single-user scope, no auth
- validate all input at the boundary

## PERFORMANCE

- progress rollup is computed incrementally

## OBSERVABILITY

- log progress recomputation with goal id + trace-id

## EXCEPTIONS

| rule | exception |
|----------|----------|
| RULE-004 | archived visions do not count as active |
