---
item: home-daily-view
module: check-in
status: draft
priority: high
depends_on: [CHECKIN-001]
---

# CHANGE

Build the Home screen (the daily check-in view) in apps/web: greeting, today's blocks as a checklist, complete/save, backed by GET /today and event append.

## WHY

This screen is opened 90% of the time and deserves the most care.

## SCOPE

### Included

- Home route with today's blocks checklist (shadcn/ui + Tailwind)
- optimistic completion via Zustand + TanStack Query
- append events through the client offline log (thin client)
- streak and score display

### Excluded

- offline sync engine (PLATFORM-003)
- dashboards and review screens

## ACCEPTANCE

### AC-001

Given today's blocks

When the user checks one and saves

Then the UI updates optimistically and an event is recorded.

## NOTES

Thin client: no domain rebuild on the frontend (ADR-002).
