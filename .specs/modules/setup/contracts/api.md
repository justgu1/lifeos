# API

## POST /setup

request:

```json
{
  "vision": { "title": "string", "statement": "string" },
  "goals": [ { "title": "string", "target_date": "date" } ],
  "blocks": [
    {
      "name": "string",
      "emoji": "string",
      "category": "string",
      "estimated_minutes": 0,
      "default_points": 0,
      "color": "string",
      "goal_id": "uuid?"
    }
  ],
  "routine": {
    "scheduled_blocks": [
      { "block_ref": "string", "weekday": 0, "start_time": "string", "mandatory": true }
    ]
  },
  "config": {
    "timezone": "string",
    "notification_hours": [0],
    "cycle_length_weeks": 0,
    "week_start_day": 0
  }
}
```

response:

```json
{
  "vision_id": "uuid",
  "goal_ids": ["uuid"],
  "cycle_id": "uuid",
  "first_week_id": "uuid"
}
```

errors:

- ALREADY_SETUP
- VALIDATION_ERROR
