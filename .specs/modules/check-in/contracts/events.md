# EVENTS

## PUBLISHED

### DayStarted

event_type: day.started

payload:

- id: uuid
- date: date
- week_id: uuid
- daily_block_ids: uuid[]

### CheckCompleted

event_type: check.completed

payload:

- day_id: uuid
- daily_block_id: uuid
- completed_at: timestamp

### DailyBlockCompleted

event_type: daily-block.completed

payload:

- daily_block_id: uuid
- block_id: uuid
- points: int
- mandatory: bool
- completed_at: timestamp

## CONSUMED

### WeekStarted

event_type: week.started

payload:

- id: uuid
- cycle_id: uuid
- start_date: date
- end_date: date

### RoutineCreated

event_type: routine.created

payload:

- id: uuid

### ScheduledBlockAdded

event_type: scheduled-block.added

payload:

- id: uuid
- block_id: uuid
