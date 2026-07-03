# DOMAIN

Setup owns no persistent entity. It is a pure orchestrator; the shape below describes the request payload only.

## SetupRequest

Not a persistent entity — this is the request shape accepted by POST /setup.

fields:

| field | type | required |
|----------|----------|----------|
| vision | object | yes |
| goals | array | yes |
| blocks | array | yes |
| scheduled_blocks | array | yes |
| config | object | yes |

rules:

- all cross-references valid before any event is appended
- idempotent (reject if already set up)
