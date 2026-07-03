---
module: routine

version: 0.1.0

depends_on: [shared-kernel, platform, strategy]

skills:
---

# PURPOSE

Routine owns the block catalog and the weekly recurring schedule. Blocks are the core execution primitive of LifeOS: the system revolves around blocks rather than tasks. This module defines what blocks exist (BlockDefinition), when they recur (ScheduledBlock), and assembles them into a published weekly Routine.

# SCOPE

includes:
- BlockDefinition catalog
- ScheduledBlock recurrence
- Routine value object
- Schedule value object
- mandatory-flag semantics

excludes:
- daily materialization (check-in owns DailyBlock)
- timeline

# FLOWS

## FLOW-001

actor: user
trigger: user defines a reusable block
result: a BlockDefinition is added to the catalog

steps:
- validate name and emoji are present
- validate estimated_minutes > 0
- optionally link to a goal_id
- create BlockDefinition aggregate
- publish BlockDefinitionCreated

## FLOW-002

actor: user
trigger: user schedules a block into the weekly routine
result: a ScheduledBlock is added

steps:
- validate block_id refers to an active block
- validate weekday and time (Monday..Saturday only)
- reject exact duplicate (weekday, start_time, block_id)
- set mandatory flag
- publish ScheduledBlockAdded

## FLOW-003

actor: user
trigger: user publishes the assembled weekly plan
result: a Routine is created

steps:
- collect scheduled_block_ids
- validate no overlapping mandatory blocks at the same time
- assign version
- publish RoutineCreated

# ENTITIES

## BlockDefinition

aggregate root describing a reusable block in the catalog.

## ScheduledBlock

placement of a block into the weekly recurring schedule.

## Routine

value object representing an assembled, versioned weekly plan.

## Schedule

value object describing weekday and time of a scheduled block.
