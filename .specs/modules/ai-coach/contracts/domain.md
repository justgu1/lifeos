# DOMAIN

## CoachSuggestion

Read model, non-authoritative.

fields:

| field | type | required |
|----------|----------|----------|
| id | uuid | yes |
| generated_at | timestamp | yes |
| context_ref | string | yes |
| text | string | yes |
| signals | json | yes |

rules:

- derived and non-authoritative
- never mutates domain state
