# RULES

## REQUIRED

- RULE-001: setup is idempotent and must be rejected if the system is already set up
- RULE-002: all-or-nothing event append in a single transaction via platform
- RULE-003: validate the entire payload at the boundary before any event is appended
- RULE-004: all cross-references (goal_id, block_ref) must resolve before any event is appended

## SECURITY

- single-user scope, no auth
- validate all input at the boundary

## PERFORMANCE

- complete the bootstrap in a single round-trip

## OBSERVABILITY

- emit one trace spanning all events emitted by the wizard

## EXCEPTIONS

| rule | exception |
|----------|----------|
| RULE-001 | none; a second setup is always rejected with ALREADY_SETUP |
