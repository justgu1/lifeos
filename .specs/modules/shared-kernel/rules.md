# RULES

## REQUIRED

- RULE-001: value objects are immutable
- RULE-002: equality is by value, not identity
- RULE-003: no I/O, no persistence, no framework imports
- RULE-004: Progress.value is always clamped to 0..100
- RULE-005: Score requires points <= max_points; percentage is derived, never stored independently

## SECURITY

- no external input reaches a value object without prior boundary validation

## PERFORMANCE

- allocation-free arithmetic; no hidden collections

## OBSERVABILITY

- not applicable (pure computation, no side effects)

## EXCEPTIONS

| rule | exception |
|----------|----------|
| RULE-005 | when max_points is 0, percentage is defined as 0 |
