---
item: vision-and-goals
module: strategy
status: draft
priority: high
depends_on: [PLATFORM-002, SHARED-001]
---

# CHANGE

Implement the Vision and Goal aggregates and GoalService: create a Vision, create Goals under it, and recompute Goal Progress from consumed events.

## WHY

Long-term direction is the top of the ladder that weekly work rolls up to.

## SCOPE

### Included

- Vision and Goal aggregates with invariants
- GoalService (create vision, create goal, recompute progress)
- event handlers for week.reviewed and daily-block.completed to update Goal progress
- unit tests for rollup and orphan-goal rejection

### Excluded

- cycles/weeks (planning)
- API endpoints (created via POST /events and POST /setup)

## ACCEPTANCE

### AC-001

Given a Vision

When a Goal is created referencing it

Then the Goal is stored with status active and derived Progress 0.

### AC-002

Given completed daily blocks linked to a Goal

When progress is recomputed

Then the Goal Progress reflects the aggregated completion.

## NOTES

Follows strategy contracts exactly. One active Vision at a time (single-user).
