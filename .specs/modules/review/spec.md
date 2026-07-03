---
module: review

version: 0.1.0

depends_on: [shared-kernel, platform, strategy, planning, check-in]

skills:
---

# PURPOSE

Review provides derived read models (week/month/cycle/year dashboards) and orchestrates the Sunday review. It owns no aggregate and no event stream; it builds projections from the event log and issues a command to planning to record WeekReviewed.

# SCOPE

includes:
- dashboard projections
- ReviewService (guides the review, issues the week.reviewed command to planning)
- GET /dashboard
- POST /review

excludes:
- owning any aggregate or event stream
- publishing domain events

# FLOWS

## FLOW-001

actor: user
trigger: Sunday review
result: week Score computed, Review inputs captured, planning commanded to publish week.reviewed

steps:
- compute the week Score from the completed vs possible points
- capture Review inputs (highlights, blockers, next_focus)
- send a command to planning's Week aggregate to record the review
- planning publishes week.reviewed, which review consumes to refresh projections

## FLOW-002

actor: user
trigger: dashboard requested for a period
result: aggregated metrics rendered for the requested period

steps:
- resolve the period (week, month, cycle, year) and reference date
- read the precomputed projection for that range
- return completed_points, possible_points, completion_rate, by_category, goal_progress, streaks

# ENTITIES

## DashboardProjection

Read model (not an aggregate) holding aggregated metrics for a period, fully rebuildable from the event log.
