# EVENTS

## PUBLISHED

### CycleCreated

event_type: cycle.created

payload:

- id: uuid
- title: string
- goal_ids: uuid[]
- start_date: date
- length_weeks: int

### WeekStarted

event_type: week.started

payload:

- id: uuid
- cycle_id: uuid
- index: int
- start_date: date
- end_date: date

### WeekReviewed

event_type: week.reviewed

payload:

- week_id: uuid
- score: Score
- review: Review
- reviewed_at: timestamp

## CONSUMED

### GoalCreated

event_type: goal.created

payload:

- id: uuid
- vision_id: uuid

### DailyBlockCompleted

event_type: daily-block.completed

payload:

- daily_block_id: uuid
- points: int
