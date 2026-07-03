# offline

Thin client (ADR-002/ADR-004): local SQLite append-only event log, outbox queue and
sync (push to POST /events + pull projections). Implemented in PLATFORM-003.
No domain rebuild happens on the client.
