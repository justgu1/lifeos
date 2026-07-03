# EVENTS

## PUBLISHED

### SnapshotCreated

event_type: snapshot.created

payload:

- aggregate_id: uuid
- aggregate_type: string
- version: int
- created_at: timestamp

## CONSUMED

Platform is the transport for all domain events. It accepts, persists and dispatches
every registered event_type to the owning module's handler via the registry. It does
not interpret payloads beyond schema validation. Registered streams:

- strategy: vision.created, goal.created
- routine: block-definition.created, scheduled-block.added, routine.created
- planning: cycle.created, week.started, week.reviewed
- check-in: day.started, check.completed, daily-block.completed
