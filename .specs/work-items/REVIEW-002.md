---
item: weekly-review-flow
module: review
status: draft
priority: medium
depends_on: [REVIEW-001, PLANNING-001]
---

# CHANGE

Implement the Sunday review flow: ReviewService computes the week Score, captures the Review inputs, and commands planning to publish week.reviewed via POST /review.

## WHY

The weekly review closes the week and feeds Goal progress and coaching.

## SCOPE

### Included

- ReviewService orchestration
- POST /review (week_id, highlights, blockers, next_focus)
- command to planning to publish week.reviewed
- already-reviewed and week-not-active rejection tests

### Excluded

- owning the Week aggregate (planning owns it)

## ACCEPTANCE

### AC-001

Given an active week

When POST /review is submitted

Then week.reviewed is published with the Score and Review, and the week becomes reviewed.

### AC-002

Given an already-reviewed week

When POST /review is submitted again

Then it returns ALREADY_REVIEWED.

## NOTES

Follows review contracts exactly. Review is on Sunday (free day).
