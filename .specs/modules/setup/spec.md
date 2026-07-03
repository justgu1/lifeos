---
module: setup

version: 0.1.0

depends_on: [strategy, routine, planning, platform]

skills:
---

# PURPOSE

Setup is the first-run wizard that orchestrates Vision -> Goals -> Blocks -> Routine -> Finish as one atomic bootstrap. It is a pure orchestrator: it owns no aggregate and publishes no domain events of its own. Instead it validates the whole payload at the boundary and, in a single transaction, emits the creation events owned by the strategy, routine, and planning modules so the user lands on an active first week.

# SCOPE

includes:
- POST /setup
- ordered command emission
- Config initialization

excludes:
- owning any aggregate
- publishing its own domain events (it emits the other modules' creation events transactionally)

# FLOWS

## FLOW-001

actor: user
trigger: user completes the first-run wizard
result: the full domain is bootstrapped atomically and the first week is active

steps:
- validate the full payload at the boundary
- reject if the system is already set up (idempotency)
- verify all cross-references are valid before any event is appended
- emit in one transaction: vision.created, goal.created (xN), block-definition.created (xN), scheduled-block.added (xN), routine.created, cycle.created, first week.started
- set Config
- return the created ids

# ENTITIES

none (orchestration).
