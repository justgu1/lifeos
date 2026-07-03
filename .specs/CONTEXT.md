# CONTEXT

## ARCHITECTURE

style:
- modular-monolith
- ddd-lite
- event-sourcing
- event-driven
- cqrs-lite
- outbox
- offline-first

layers:
- presentation
- application
- domain
- infrastructure

ownership:
- event-stream-equals-aggregate
- event-published-by-aggregate-owner
- other-modules-consume-events-or-send-commands
- platform-routes-events-via-handler-registry

## STACK

runtime:
- python-3.12
- node-20

framework:
- api: fastapi, sqlalchemy, alembic
- web: react, vite, typescript, capacitor, tanstack-query, zustand, tailwind, shadcn-ui

database:
- sqlite

infra:
- docker

monorepo:
layout:
- apps/api
- apps/web
- packages/domain
- packages/shared
- infra/docker

toolchain:
- python: uv-workspace
- typescript: pnpm-workspace

placement:
- shared-kernel: packages/shared + packages/domain
- domain-modules: packages/domain
- platform-and-endpoints: apps/api
- ui-flows: apps/web

## LANGUAGE

code: en
comments: en
specs: en
docs: pt-BR

## NAMING

files: kebab-case
classes: PascalCase
functions: camelCase
variables: camelCase
constants: UPPER_SNAKE_CASE
events: PascalCase-past-tense
event-type: dotted-lowercase (aggregate.past-tense, e.g. goal.created)
aggregate-stream-id: aggregate_type:aggregate_id

exceptions:
- python-identifiers-use-snake_case (PEP8) for functions and variables

## GLOBAL_CONSTRAINTS

security:
- validate-input-at-boundary
- never-log-sensitive-data
- no-secrets-in-event-payload
- single-user-auth-model

performance:
- indexed-queries
- paginated-lists
- snapshot-bounded-replay
- reads-served-from-projections
- hot-path-get-today-low-latency

observability:
- trace-id-required
- structured-logging
- outbox-lag-metric
- projection-lag-metric

delivery:
- one-work-item-one-pr
- ci-gate: unit-tests + e2e-tests + apk-build
- merge-only-on-green-ci

## ADRS

### ADR-001

status: accepted
date: 2026-07-03
decision: Adopt Event Sourcing as the system of record. All state changes are immutable events appended to the Events table; aggregates are rebuilt by replay.
reason: Full history enables dashboards, weekly review and AI coaching; append-only log makes offline sync natural.
consequences: Requires snapshots to bound replay cost, read-model projections, and disciplined event/schema versioning.

### ADR-002

status: accepted
date: 2026-07-03
decision: The authoritative pure domain lives in Python (packages/domain). The web/offline client is thin (append events + local outbox + optimistic UI) with no TS domain mirror. Event payloads are defined once as JSON Schema in packages/shared/schema and code-generated into pydantic (packages/shared/py) and TS types + zod (packages/shared/ts).
reason: One authoritative implementation of replay/invariants avoids divergence bugs; a shared generated contract keeps the event schema identical across backend and frontend.
consequences: A codegen step is required; the client cannot rebuild aggregates authoritatively and reconciles via server projections.

### ADR-003

status: accepted
date: 2026-07-03
decision: Use per-aggregate latest-only snapshots. Snapshot cadence is weekly (aligned to the Sunday review) plus a safety threshold of every N events. Snapshotting emits SnapshotCreated.
reason: Bounds cold-read replay cost on SQLite and mobile.
consequences: Read path is always snapshot + tail replay; a stale/missing snapshot is correct but slower.

### ADR-004

status: accepted
date: 2026-07-03
decision: Offline-first with a single write path via POST /events. The client records events locally and replays them to POST /events; the server is the authoritative merger, deduplicating by event id and enforcing optimistic concurrency via version.
reason: 90% of usage is the daily check-in, which must work offline on Capacitor.
consequences: Ingestion must be idempotent; delivery is at-least-once; conflicts return 409 for reconciliation.

### ADR-005

status: accepted
date: 2026-07-03
decision: CQRS-lite. Reads (GET /today, GET /week, GET /dashboard) are served from read-model projections, never from live replay on the hot path.
reason: Performance and a fast daily check-in.
consequences: Projections must be rebuildable from the event log and kept in sync on append.

### ADR-006

status: accepted
date: 2026-07-03
decision: Governance — one work-item equals one branch and one pull request. Every PR must pass a mandatory CI pipeline: unit tests, end-to-end tests, and Capacitor APK build. Merge only on green CI.
reason: Keeps changes atomic, reviewable and always shippable to a mobile artifact.
consequences: Each work-item is scoped to be independently mergeable; CI workflows live in .github/workflows.

## INTEGRATIONS

| service | purpose | owner |
|----------|----------|----------|
| Capacitor Local Notifications | daily check-in reminders (13h/18h/22h) | notifications |
| AI provider (deferred) | insights and coaching over events/snapshots | ai-coach |

## GLOSSARY

| term | definition |
|----------|----------|
| Vision | Long-term direction statement that goals ladder up to |
| Goal | Long-term objective belonging to a Vision, with derived Progress |
| Cycle | Medium-term horizon (calendar-quarter default, configurable) grouping Weeks toward Goals |
| Week | Mon-Sun period inside a Cycle; Mon-Sat hold blocks, Sunday is free/review |
| Day | A single day owning materialized DailyBlocks and a Score |
| Block | Reusable unit of focused activity; the system revolves around blocks, not tasks |
| BlockDefinition | Catalog entry for a block (name, emoji, category, estimated_minutes, default_points, color, active) |
| ScheduledBlock | A BlockDefinition placed on a weekday/time in the weekly routine, with a mandatory flag |
| DailyBlock | A ScheduledBlock materialized for a concrete Day; can be completed/skipped |
| Routine | The assembled weekly plan of ScheduledBlocks (value object) |
| Schedule | Weekday + time placement of a block (value object) |
| Progress | Normalized 0-100 completion measure (value object) |
| Score | Points achieved vs possible with derived percentage (value object) |
| Review | The recorded outcome of a weekly review (value object on Week) |
| Notification | A scheduled reminder (value object) |
| Event | An immutable fact appended to the event store |
| Snapshot | A materialized aggregate state at a version, to bound replay |
| Outbox | Transactional queue of events pending delivery/sync |
| Config | Singleton settings (timezone, notification hours, week start, cycle length) |
| Aggregate | Consistency boundary rebuilt from its event stream |
| Projection | A read model derived from events |
| Ladder-up | The linkage from daily blocks through weeks/cycles to goals and vision |
| Check-in | The daily act of completing blocks |
| Mandatory block | A ScheduledBlock flagged as required, tracked with its own completion rate |
| Streak | Count of consecutive days meeting the completion criterion |
