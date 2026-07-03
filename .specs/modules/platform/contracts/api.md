# API

## POST /events

request:

```json
{
  "events": [
    {
      "id": "ulid",
      "aggregate_id": "uuid",
      "aggregate_type": "string",
      "expected_version": 0,
      "event_type": "aggregate.past-tense",
      "schema_version": 1,
      "payload": {},
      "created_at": "ISO-8601"
    }
  ]
}
```

response:

```json
{
  "accepted": ["ulid"],
  "conflicts": [{ "id": "ulid", "reason": "VERSION_CONFLICT" }]
}
```

errors:
- VALIDATION_ERROR
- VERSION_CONFLICT (HTTP 409)
- DUPLICATE_EVENT (idempotent; returned as accepted)
- UNKNOWN_EVENT_TYPE
