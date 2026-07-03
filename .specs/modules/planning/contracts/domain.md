# DOMAIN

## Cycle

fields:

| field | type | required |
|----------|----------|----------|
| id | uuid | yes |
| title | string | yes |
| goal_ids | uuid[] | yes |
| start_date | date | yes |
| length_weeks | int>0 | yes |
| status | enum(active,completed,archived) | yes |
| progress | Progress | yes |

rules:

- length_weeks > 0
- default aligned to calendar quarter
- start_date aligns to week_start_day (Monday)
- progress is derived
- immutable id

## Week

fields:

| field | type | required |
|----------|----------|----------|
| id | uuid | yes |
| cycle_id | uuid | yes |
| index | int | yes |
| start_date | date | yes |
| end_date | date | yes |
| status | enum(planned,active,reviewed) | yes |
| score | Score | yes |
| review | Review | no |

rules:

- spans exactly 7 days Monday..Sunday
- belongs to one Cycle
- Sunday holds no blocks
- immutable id

## Review

fields:

| field | type | required |
|----------|----------|----------|
| week_id | uuid | yes |
| score | Score | yes |
| highlights | text | no |
| blockers | text | no |
| next_focus | text | no |
| reviewed_at | timestamp | yes |

rules:

- set once, only on reviewed status
- value object (no independent identity)
