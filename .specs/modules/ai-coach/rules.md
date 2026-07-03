# RULES

## REQUIRED

- RULE-001: AI Coach is read-only over the domain
- RULE-002: AI Coach never auto-mutates aggregates or executes changes
- RULE-003: CoachSuggestion is derived and non-authoritative
- RULE-004: implementation is deferred until its work-item is prioritized

## SECURITY

- single-user scope, no auth
- no sensitive data leaves the device without consent
- document the external-provider data boundary

## PERFORMANCE

- analysis runs off the read side, never blocking the write path

## OBSERVABILITY

- log model/provider and latency for each generation

## EXCEPTIONS

| rule | exception |
|----------|----------|
| RULE-004 | none until the work-item is prioritized |
