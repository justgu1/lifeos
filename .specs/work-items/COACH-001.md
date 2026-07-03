---
item: ai-insights-coach
module: ai-coach
status: draft
priority: low
depends_on: [REVIEW-002, PLATFORM-003]
---

# CHANGE

Implement the AI coach: consume events, snapshots and context to generate read-only insights and suggestions (weekly summary and on-demand nudges).

## WHY

Once history exists, AI can surface patterns and coach the user toward goals.

## SCOPE

### Included

- context assembly from events + snapshots + projections
- weekly coaching summary on week.reviewed and on-demand nudge
- CoachSuggestion read model and GET /coach
- provider integration with a documented data boundary

### Excluded

- any mutation of domain aggregates (read-only)

## ACCEPTANCE

### AC-001

Given a reviewed week

When the coach runs

Then a CoachSuggestion is generated from the history without mutating any aggregate.

## NOTES

Follows ai-coach contracts. Built last; no sensitive data leaves the device without consent.
