# EVENTS

## PUBLISHED

none — review is a read side and publishes no domain events. The state change for a review is performed by planning's Week aggregate, which publishes week.reviewed.

## CONSUMED

### DailyBlockCompleted

event_type: daily-block.completed

payload:

- id: ulid

### CheckCompleted

event_type: check.completed

payload:

- id: ulid

### WeekStarted

event_type: week.started

payload:

- id: ulid

### WeekReviewed

event_type: week.reviewed

payload:

- id: ulid

### CycleCreated

event_type: cycle.created

payload:

- id: ulid

### GoalCreated

event_type: goal.created

payload:

- id: ulid

### VisionCreated

event_type: vision.created

payload:

- id: ulid
