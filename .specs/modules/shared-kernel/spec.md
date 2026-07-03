---
module: shared-kernel

version: 0.1.0

depends_on: []

skills:
---

# PURPOSE

Provide the canonical value objects shared across all bounded contexts, with no dependency on persistence, transport or any aggregate.

# SCOPE

includes:
- Progress value object
- Score value object
- value-object arithmetic and comparison

excludes:
- aggregates
- persistence
- API endpoints
- events

# FLOWS

## FLOW-001

actor: any domain service
trigger: a completion measure must be normalized
result: a Progress value clamped to 0..100

steps:
- receive completed and total counts
- compute ratio guarding division by zero
- return immutable Progress

## FLOW-002

actor: any domain service
trigger: points must be aggregated into a Score
result: a Score with derived percentage

steps:
- receive achieved points and possible points
- validate points <= max_points
- derive percentage
- return immutable Score

# ENTITIES

## Progress

value object; immutable; equality by value.

## Score

value object; immutable; equality by value.
