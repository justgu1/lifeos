---
item: month-cycle-year-dashboards
module: review
status: draft
priority: medium
depends_on: [REVIEW-002]
---

# CHANGE

Extend the dashboard projections and GET /dashboard to the month, cycle and year periods, including goal progress rollups.

## WHY

The user needs longer horizons to see cycle and yearly progress toward goals.

## SCOPE

### Included

- month, cycle and year period projections
- goal_progress and streaks across periods
- GET /dashboard?period=month|cycle|year
- parity tests per period

### Excluded

- AI insights (COACH-001)

## ACCEPTANCE

### AC-001

Given several reviewed weeks in a cycle

When GET /dashboard?period=cycle is called

Then it aggregates weeks and reports goal progress.

## NOTES

Follows review contracts exactly.
