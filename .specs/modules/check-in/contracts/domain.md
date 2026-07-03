# DOMAIN

## Day

fields:

| field | type | required |
|----------|----------|----------|
| id | uuid | yes |
| date | date | yes |
| week_id | uuid | yes |
| status | enum(pending,started,closed) | yes |
| score | Score | yes |

rules:

- one Day per date
- belongs to the active Week
- Sunday materializes no DailyBlocks
- immutable id

## DailyBlock

fields:

| field | type | required |
|----------|----------|----------|
| id | uuid | yes |
| day_id | uuid | yes |
| block_id | uuid | yes |
| scheduled_block_id | uuid | no |
| name | string | yes |
| emoji | string | yes |
| planned_start | HH:MM | no |
| estimated_minutes | int | yes |
| points | int | yes |
| mandatory | bool | yes |
| status | enum(pending,completed,skipped) | yes |
| completed_at | timestamp | no |

rules:

- block_id resolves to a BlockDefinition
- points snapshotted from default_points at materialization (immutable to later catalog edits)
- completion is idempotent
- immutable id
