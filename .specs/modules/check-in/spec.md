---
module: check-in

version: 0.1.0

depends_on: [shared-kernel, platform, routine, planning]

skills:
---

# PURPOSE

Check-in is the daily execution surface: it materializes the day's blocks from the routine and lets the user check them off. This is the 90% flow behind the Home screen and the system's hot path. It owns the Day aggregate and its DailyBlocks, and serves the today board read model.

# SCOPE

includes:
- Day aggregate
- DailyBlock materialization and completion
- CheckService
- GET /today

excludes:
- recurrence rules (routine)
- week aggregation (planning)

# FLOWS

## FLOW-001

actor: user
trigger: user opens or starts the day
result: DailyBlocks are materialized from the routine and the day is started

steps:
- resolve the active Week for the date
- call PlannerService for the weekday's scheduled blocks
- materialize DailyBlocks (skip Sunday)
- snapshot points from each BlockDefinition default_points
- create Day aggregate with status started
- publish DayStarted

## FLOW-002

actor: user
trigger: user completes a DailyBlock
result: the block is marked completed and Score is awarded

steps:
- validate the block belongs to this Day
- apply idempotent completion (no-op if already completed)
- set completed_at and status completed
- award Score to the Day
- publish DailyBlockCompleted and CheckCompleted

## FLOW-003

actor: user
trigger: user reads the today board
result: today's blocks, score and streak are returned

steps:
- resolve today's Day projection
- return blocks, score and streak from a single indexed read

# ENTITIES

## Day

aggregate root representing one calendar date of execution.

## DailyBlock

entity representing a materialized block on a Day, checkable by the user.
