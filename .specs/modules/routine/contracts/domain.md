# DOMAIN

## BlockDefinition

fields:

| field | type | required |
|----------|----------|----------|
| id | uuid | yes |
| name | string | yes |
| emoji | string | yes |
| category | string | yes |
| estimated_minutes | int>0 | yes |
| default_points | int>=0 | yes |
| color | string | yes |
| active | bool | yes |
| goal_id | uuid | no |

rules:

- name+emoji required
- estimated_minutes>0
- deactivating never deletes history

## ScheduledBlock

fields:

| field | type | required |
|----------|----------|----------|
| id | uuid | yes |
| block_id | uuid | yes |
| schedule | Schedule | yes |
| mandatory | bool | yes |

rules:

- block_id must be active
- no exact duplicate (weekday,start_time,block_id)
- blocks scheduled Monday..Saturday only (Sunday is free)

## Schedule

fields:

| field | type | required |
|----------|----------|----------|
| weekday | int(0..6) | yes |
| start_time | HH:MM | yes |
| end_time | HH:MM | no |

rules:

- valid weekday/time
- end_time>start_time when present
- weekday 6 (Sunday) not allowed for scheduled blocks

## Routine

fields:

| field | type | required |
|----------|----------|----------|
| name | string | yes |
| scheduled_block_ids | uuid[] | yes |
| version | int | yes |

rules:

- no overlapping mandatory blocks at the same time
