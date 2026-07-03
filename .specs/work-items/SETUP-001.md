---
item: setup-wizard
module: setup
status: draft
priority: high
depends_on: [PLANNING-001]
---

# CHANGE

Implement the first-run wizard endpoint POST /setup that validates the full payload and atomically emits the creation events (vision, goals, blocks, scheduled blocks, routine, cycle, first week) and initializes Config.

## WHY

The wizard is the single onboarding flow (Vision -> Goals -> Blocks -> Routine -> Finish) that seeds the whole system in one step.

## SCOPE

### Included

- POST /setup with full payload validation
- ordered, all-or-nothing event emission via platform in one transaction
- Config initialization (timezone, notification_hours, cycle_length_weeks, week_start_day)
- idempotency (reject if already set up)
- tests for rollback, idempotency and resulting active first week

### Excluded

- editing existing setup (out of scope for this phase)

## ACCEPTANCE

### AC-001

Given a valid setup payload

When POST /setup is called

Then all creation events are appended atomically and ids are returned.

### AC-002

Given the system is already set up

When POST /setup is called again

Then it returns ALREADY_SETUP and appends nothing.

## NOTES

Follows setup contracts exactly. Setup owns no aggregate; it orchestrates other modules' events.
