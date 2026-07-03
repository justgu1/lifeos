# DOMAIN

## Vision

fields:

| field | type | required |
|----------|----------|----------|
| id | uuid | yes |
| title | string | yes |
| statement | string | no |
| active | bool | yes |
| created_at | timestamp | yes |

rules:

- title required
- one active vision at a time (single-user)
- immutable id

## Goal

fields:

| field | type | required |
|----------|----------|----------|
| id | uuid | yes |
| vision_id | uuid | yes |
| title | string | yes |
| description | string | no |
| target_date | date | no |
| progress | Progress | yes |
| status | enum(active,achieved,archived) | yes |
| created_at | timestamp | yes |

rules:

- vision_id must exist
- progress is a projection, never set directly
- progress is derived
