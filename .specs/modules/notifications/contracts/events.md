# EVENTS

## PUBLISHED

Optional/internal events; not part of the domain event contract.

### NotificationScheduled

event_type: notification.scheduled

payload:

- id: uuid
- type: enum(midday,evening,night)
- scheduled_for: timestamp

### NotificationSent

event_type: notification.sent

payload:

- id: uuid
- sent_at: timestamp

## CONSUMED

### DayStarted

event_type: day.started

payload:

- id: ulid

### WeekStarted

event_type: week.started

payload:

- id: ulid

### DailyBlockCompleted

event_type: daily-block.completed

payload:

- id: ulid
