# EVENTS

## PUBLISHED

### CoachSuggestionCreated

optional.

event_type: coach-suggestion.created

payload:

- id: uuid
- generated_at: timestamp
- context_ref: string

## CONSUMED

### WeekReviewed

event_type: week.reviewed

payload:

- week_id: uuid

### DailyBlockCompleted

event_type: daily-block.completed

payload:

- daily_block_id: uuid

### CheckCompleted

event_type: check.completed

payload:

- check_id: uuid
