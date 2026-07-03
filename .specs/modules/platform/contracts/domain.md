# DOMAIN

## EventRecord

fields:

| field | type | required |
|----------|----------|----------|
| id | ulid | yes |
| aggregate_id | uuid | yes |
| aggregate_type | string | yes |
| version | int (1-based) | yes |
| event_type | string (dotted) | yes |
| payload | json | yes |
| schema_version | int | yes |
| created_at | timestamp (ISO-8601 UTC) | yes |

rules:

- unique id (idempotency)
- unique (aggregate_id, version), contiguous per aggregate
- append-only (no update/delete)
- payload validated against packages/shared/schema

## Snapshot

fields:

| field | type | required |
|----------|----------|----------|
| aggregate_id | uuid | yes |
| aggregate_type | string | yes |
| version | int | yes |
| payload | json | yes |
| created_at | timestamp | yes |

rules:

- one latest snapshot per aggregate
- version <= max event version for the aggregate

## OutboxItem

fields:

| field | type | required |
|----------|----------|----------|
| id | ulid | yes |
| payload | json | yes |
| status | enum(pending, sent, failed) | yes |
| attempts | int (>=0) | yes |
| last_error | string | no |
| created_at | timestamp | yes |
| synced_at | timestamp | no |

rules:

- status transitions move forward only
- written in the same transaction as the events it carries

## Config

fields:

| field | type | required |
|----------|----------|----------|
| timezone | string (IANA) | yes |
| notification_hours | int[] | yes |
| week_start_day | enum(monday) | yes |
| cycle_length_weeks | int (>0) | yes |
| flags | json | no |

rules:

- singleton
- notification_hours default [13, 18, 22]
- week_start_day default monday
- cycle_length_weeks default aligned to calendar quarter
