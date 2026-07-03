---
item: event-schema-and-shared-kernel
module: shared-kernel
status: draft
priority: high
depends_on: [PLATFORM-001]
---

# CHANGE

Author the cross-language event schema (JSON Schema per event in packages/shared/schema), the codegen into pydantic (packages/shared/py) and TS types + zod (packages/shared/ts), and implement the shared-kernel value objects Progress and Score.

## WHY

Every module's events must validate identically on backend and frontend (ADR-002). Progress and Score are used by strategy, planning, check-in and review, so they must exist before those modules.

## SCOPE

### Included

- JSON Schema for the canonical event catalog
- codegen pipeline (schema -> pydantic, schema -> ts+zod) wired to a root script
- Progress and Score value objects with clamping and derived percentage
- unit tests for boundary values and schema/codegen round-trip

### Excluded

- event persistence (PLATFORM-002)
- any aggregate

## ACCEPTANCE

### AC-001

Given the JSON Schema source

When codegen runs

Then pydantic models and TS zod validators are generated and match the schema.

### AC-002

Given points and max_points

When a Score is built

Then percentage is derived correctly, including max_points = 0 yielding 0.

## NOTES

Follows shared-kernel contracts/domain.md exactly.
