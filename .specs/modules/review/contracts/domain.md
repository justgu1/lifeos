# DOMAIN

## DashboardProjection

fields:

| field | type | required |
|----------|----------|----------|
| period | enum(week,month,cycle,year) | yes |
| range | string | yes |
| completed_points | int | yes |
| possible_points | int | yes |
| completion_rate | int(0..100) | yes |
| by_category | json | yes |
| goal_progress | json | yes |
| streaks | json | yes |

rules:

- derived only
- fully rebuildable from the event log
- never authoritative
