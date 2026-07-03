---
item: cycle-week-timeline
module: planning
status: draft
priority: high
depends_on: [ROUTINE-001]
---

# CHANGE

Implement the Cycle and Week aggregates, the Review value object, PlannerService (blocks scheduled for a date), Week Score aggregation, and the GET /week read.

## WHY

Cycles and Weeks are the timeline connecting daily execution to long-term goals.

## SCOPE

### Included

- Cycle aggregate (calendar-quarter default, cycle_length_weeks configurable)
- Week aggregate (Mon..Sun, status planned/active/reviewed, Score, Review)
- PlannerService: compute ScheduledBlocks for a given date
- Week Score aggregation from consumed daily-block.completed
- WeekReviewed published on command from review's ReviewService
- GET /week projection

### Excluded

- Day/DailyBlock (check-in)
- dashboards (review)

## ACCEPTANCE

### AC-001

Given a Cycle

When a Week is started

Then it spans Monday..Sunday and status becomes active.

### AC-002

Given completed daily blocks in a week

When the week Score is read

Then it aggregates the DailyBlock Scores.

## NOTES

Follows planning contracts exactly. WeekReviewed is owned here but triggered by ReviewService.
