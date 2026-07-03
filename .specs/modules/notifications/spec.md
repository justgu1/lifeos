---
module: notifications

version: 0.1.0

depends_on: [platform, planning, check-in]

skills:
---

# PURPOSE

Notifications delivers time-based reminders (default 13h/18h/22h) driven by Config, opening the check-in when a reminder fires.

# SCOPE

includes:
- Notification value object
- NotificationService
- scheduling and dispatch
- quiet-hours and suppression

excludes:
- device push transport specifics beyond a port

# FLOWS

## FLOW-001

actor: system
trigger: day.started
result: the day's reminders are scheduled

steps:
- read notification_hours from Config (default [13,18,22])
- resolve timezone and quiet hours
- batch-schedule one Notification per configured hour for the day
- publish NotificationScheduled for each

## FLOW-002

actor: system
trigger: a configured hour is reached
result: a reminder fires only if pending blocks remain, opening the check-in

steps:
- at the scheduled hour, check for pending blocks
- if zero pending, mark the Notification skipped and stop
- otherwise dispatch the reminder and mark it sent
- the reminder opens the check-in directly

# ENTITIES

## Notification

Value object describing a single scheduled reminder for a given hour, its payload and delivery status.
