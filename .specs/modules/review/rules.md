# RULES

## REQUIRED

- RULE-001: projections must be rebuildable from the event log; no authoritative state is held here
- RULE-002: POST /review delegates the state change to planning's Week aggregate via a command; review never mutates the Week directly
- RULE-003: the weekly review happens on Sunday
- RULE-004: review publishes no domain events; it only consumes and issues commands

## SECURITY

- single-user, no auth; no cross-user data access

## PERFORMANCE

- dashboards are served from precomputed projections, not live event replay

## OBSERVABILITY

- expose a projection-lag metric
- log projection rebuilds

## EXCEPTIONS

| rule | exception |
|----------|----------|
