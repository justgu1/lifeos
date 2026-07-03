---
item: weekly-dashboard
module: review
status: draft
priority: medium
depends_on: [CHECKIN-001]
---

# CHANGE

Build the weekly dashboard projection and the GET /dashboard endpoint for the week period, aggregating completion, points and streaks from events.

## WHY

The user needs a weekly view of progress derived from daily check-ins.

## SCOPE

### Included

- week-period DashboardProjection builder from consumed events
- GET /dashboard?period=week
- projection-equals-replay parity tests

### Excluded

- month/cycle/year dashboards (REVIEW-003)
- the weekly review flow (REVIEW-002)

## ACCEPTANCE

### AC-001

Given a week of completed blocks

When GET /dashboard?period=week is called

Then completion_rate, points and by_category reflect the events.

## NOTES

Follows review contracts exactly. Projections are rebuildable from the log.
