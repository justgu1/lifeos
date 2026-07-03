# EVENTS

## PUBLISHED

### VisionCreated

event_type: vision.created

payload:

- id: uuid
- title: string
- statement: string
- created_at: timestamp

### GoalCreated

event_type: goal.created

payload:

- id: uuid
- vision_id: uuid
- title: string
- target_date: date
- created_at: timestamp

### GoalAchieved

event_type: goal.achieved

payload:

- id: uuid
- achieved_at: timestamp

## CONSUMED

### WeekReviewed

event_type: week.reviewed

payload:

- week_id: uuid

### DailyBlockCompleted

event_type: daily-block.completed

payload:

- daily_block_id: uuid
