---
item: checkin-notifications
module: notifications
status: draft
priority: medium
depends_on: [CHECKIN-001]
---

# CHANGE

Implement Capacitor local notifications at the configured hours (13h/18h/22h) that open the check-in directly, scheduled on day.started and suppressed when no blocks remain pending.

## WHY

Timely reminders drive the daily check-in habit.

## SCOPE

### Included

- NotificationService: schedule the day's reminders on day.started
- fire only if pending blocks remain (honor timezone and quiet hours)
- Capacitor local notification integration opening the check-in
- tests for timezone correctness and suppression when complete

### Excluded

- push notifications from a server (local only this phase)

## ACCEPTANCE

### AC-001

Given a started day with pending blocks

When a configured hour arrives

Then a notification fires and opens the check-in.

### AC-002

Given all blocks complete

When a configured hour arrives

Then no notification fires.

## NOTES

Follows notifications contracts exactly. Hours come from Config.
