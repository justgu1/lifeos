# EVENTS

## PUBLISHED

### BlockDefinitionCreated

event_type: block-definition.created

payload:

- id: uuid
- name: string
- emoji: string
- category: string
- estimated_minutes: int
- default_points: int
- color: string
- goal_id: uuid

### ScheduledBlockAdded

event_type: scheduled-block.added

payload:

- id: uuid
- block_id: uuid
- weekday: int
- start_time: string
- mandatory: bool

### RoutineCreated

event_type: routine.created

payload:

- routine_id: uuid
- scheduled_block_ids: uuid[]
- created_at: timestamp

## CONSUMED

### GoalCreated

event_type: goal.created

payload:

- id: uuid
- vision_id: uuid
- title: string
- target_date: date
- created_at: timestamp
