# API

## GET /today

request:

```json
{}
```

response:

```json
{
  "day": {},
  "blocks": [
    {
      "id": "uuid",
      "name": "string",
      "emoji": "string",
      "planned_start": "HH:MM",
      "points": 0,
      "mandatory": true,
      "status": "pending"
    }
  ],
  "score": {},
  "streak": 0
}
```

errors:
- DAY_NOT_FOUND
