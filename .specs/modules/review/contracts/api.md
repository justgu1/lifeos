# API

## GET /dashboard

request:

```json
{
  "period": "week",
  "ref": "2026-07-03"
}
```

response:

```json
{
  "period": "week",
  "range": "2026-06-29/2026-07-05",
  "completed_points": 42,
  "possible_points": 60,
  "completion_rate": 70,
  "by_category": {},
  "goal_progress": {},
  "streaks": {}
}
```

errors:
- INVALID_PERIOD

## POST /review

request:

```json
{
  "week_id": "uuid",
  "highlights": "string",
  "blockers": "string",
  "next_focus": "string"
}
```

response:

```json
{
  "week_id": "uuid",
  "score": 70,
  "reviewed_at": "2026-07-05T18:00:00Z"
}
```

errors:
- WEEK_NOT_ACTIVE
- ALREADY_REVIEWED
