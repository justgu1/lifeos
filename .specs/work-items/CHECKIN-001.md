---
item: day-dailyblock-checkin
module: check-in
status: draft
priority: high
depends_on: [PLANNING-001]
---

# CHANGE

Implement the Day aggregate, DailyBlock materialization from the routine, completion with Score, CheckService, and the GET /today read model.

## WHY

The daily check-in is the 90% flow; it must be fast and correct.

## SCOPE

### Included

- Day aggregate and DailyBlock entity
- lazy materialization from ScheduledBlocks for the weekday (Sunday materializes none)
- idempotent completion, points snapshotted at materialization
- CheckService and its events (day.started, check.completed, daily-block.completed)
- GET /today projection with day, blocks, score, streak

### Excluded

- Home UI (CHECKIN-002)
- dashboards (review)

## ACCEPTANCE

### AC-001

Given an active week and a weekday with scheduled blocks

When the day is opened

Then DailyBlocks are materialized deterministically and day.started is emitted.

### AC-002

Given a DailyBlock

When completed twice

Then completion is idempotent and Score is awarded once.

## NOTES

Follows check-in contracts exactly.
