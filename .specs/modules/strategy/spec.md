---
module: strategy

version: 0.1.0

depends_on: [shared-kernel, platform]

skills:
---

# PURPOSE

Strategy owns the long-term direction of the system: a single active Vision and the Goals that ladder up to it. It provides the north star that weekly execution work aligns with, and it maintains derived Goal progress so higher-level intent stays connected to daily activity.

# SCOPE

includes:
- Vision lifecycle
- Goal lifecycle
- Goal Progress rollup

excludes:
- cycles
- weeks
- blocks
- daily execution

# FLOWS

## FLOW-001

actor: user
trigger: user defines a long-term direction
result: an active Vision is created

steps:
- validate title is present
- ensure no other active vision exists
- create Vision aggregate
- publish VisionCreated

## FLOW-002

actor: user
trigger: user defines a goal under a vision
result: a Goal is created linked to the vision

steps:
- validate vision_id exists
- validate title is present
- accept optional target_date
- create Goal aggregate with derived progress
- publish GoalCreated

## FLOW-003

actor: system
trigger: consuming week.reviewed or daily-block.completed
result: Goal progress is recomputed

steps:
- receive WeekReviewed or DailyBlockCompleted event
- resolve affected goal(s)
- recompute Progress projection incrementally
- update Goal progress
- publish GoalAchieved when progress reaches completion

# ENTITIES

## Vision

aggregate root holding the single active long-term direction.

## Goal

aggregate root representing a measurable objective under a Vision.
