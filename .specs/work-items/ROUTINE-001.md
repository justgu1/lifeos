---
item: block-catalog-and-routine
module: routine
status: draft
priority: high
depends_on: [STRATEGY-001]
---

# CHANGE

Implement the BlockDefinition catalog, ScheduledBlock recurrence, the Routine and Schedule value objects and RoutineService, all event-sourced.

## WHY

The system revolves around blocks; the catalog and weekly schedule are the core execution primitive reused by planning and check-in.

## SCOPE

### Included

- BlockDefinition aggregate (name, emoji, category, estimated_minutes, default_points, color, active, optional goal_id)
- ScheduledBlock (weekday Mon..Sat, time, mandatory) with overlap/duplicate validation
- Routine and Schedule value objects
- RoutineService and its events (block-definition.created, scheduled-block.added, routine.created)
- unit tests for overlap detection and mandatory semantics

### Excluded

- daily materialization (check-in owns DailyBlock)
- Sunday scheduling (Sunday is free)

## ACCEPTANCE

### AC-001

Given an active BlockDefinition

When it is scheduled on a weekday and time

Then a ScheduledBlock is created, rejecting exact duplicates and Sunday.

### AC-002

Given two mandatory blocks at the same time

When assembling a Routine

Then the overlap is rejected.

## NOTES

Follows routine contracts exactly.
