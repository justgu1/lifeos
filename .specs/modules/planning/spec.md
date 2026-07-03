---
module: planning

version: 0.1.0

depends_on: [shared-kernel, platform, strategy, routine]

skills:
---

# PURPOSE

Planning owns the medium-term timeline: Cycles that group Weeks toward Goals, and the weekly review record. It owns the Week aggregate and therefore publishes WeekReviewed (on command from the review flow's ReviewService). It provides the PlannerService that computes which blocks are scheduled for a given date and serves the week read model.

# SCOPE

includes:
- Cycle creation
- Week start and rollover
- Week Score and Review
- PlannerService (compute blocks scheduled for a date)
- GET /week

excludes:
- Day and DailyBlock (check-in)
- dashboards (review)

# FLOWS

## FLOW-001

actor: user
trigger: user creates a cycle targeting goals
result: an active Cycle is created

steps:
- validate title is present
- validate goal_ids exist
- resolve length_weeks from Config default unless overridden
- align start_date to week_start_day (Monday), default to calendar quarter
- create Cycle aggregate
- publish CycleCreated

## FLOW-002

actor: system
trigger: a new week begins in an active cycle
result: a Week is started spanning Monday..Sunday

steps:
- resolve active Cycle
- compute next week index and start_date/end_date (Mon..Sun)
- create Week aggregate with status planned then active
- publish WeekStarted

## FLOW-003

actor: system
trigger: ReviewService issues a record-review command
result: the Week review is recorded with a Review VO and weekly Score

steps:
- receive record-review command from ReviewService
- validate the Week is being reviewed
- aggregate DailyBlock Scores into the weekly Score
- attach Review value object and set status reviewed
- publish WeekReviewed

# ENTITIES

## Cycle

aggregate root grouping Weeks toward Goals over a configurable span.

## Week

aggregate root representing one Monday..Sunday span within a Cycle.

## Review

value object capturing the outcome of a weekly review.
