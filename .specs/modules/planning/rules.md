# RULES

## REQUIRED

- RULE-001: WeekReviewed is published only via a ReviewService command
- RULE-002: Cycle length_weeks comes from Config default unless explicitly overridden
- RULE-003: Week Score is the aggregation of its DailyBlock Scores
- RULE-004: a Week spans exactly 7 days Monday..Sunday and belongs to one Cycle
- RULE-005: Sunday holds no blocks and is reserved for the weekly review
- RULE-006: Review is set once, only on reviewed status

## SECURITY

- single-user scope, no auth
- validate all input at the boundary

## PERFORMANCE

- week read is served from a projection/snapshot

## OBSERVABILITY

- log week transitions with cycle id + trace-id

## EXCEPTIONS

| rule | exception |
|----------|----------|
| RULE-002 | length_weeks may be overridden per Cycle at creation |
| RULE-005 | none |
