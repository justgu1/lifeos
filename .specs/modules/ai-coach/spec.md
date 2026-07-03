---
module: ai-coach

version: 0.1.0

depends_on: [shared-kernel, platform, strategy, planning, check-in, review]

skills:
---

# PURPOSE

AI Coach (built last) generates coaching insights and suggestions from history — events, snapshots, and surrounding context. It is strictly read-only over the domain: it analyzes projections and the event log to surface nudges and weekly summaries, but never mutates aggregates and never auto-executes changes.

# SCOPE

includes:
- read-only analysis over events/projections
- suggestion generation

excludes:
- mutating aggregates
- auto-executing changes

# FLOWS

## FLOW-001

actor: system
trigger: week.reviewed
result: a weekly coaching summary is generated

steps:
- receive WeekReviewed event
- gather the week's events, snapshots, and context
- analyze signals read-only
- generate a coaching summary as a CoachSuggestion
- optionally publish CoachSuggestionCreated

## FLOW-002

actor: user
trigger: user requests an on-demand nudge
result: a contextual suggestion is generated

steps:
- gather recent events and current projections
- analyze signals read-only
- generate a nudge as a CoachSuggestion
- return the suggestion

# ENTITIES

## CoachSuggestion

read model holding a derived, non-authoritative coaching suggestion.
