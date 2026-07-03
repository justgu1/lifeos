# @lifeos/shared

Cross-language contract for LifeOS domain events.

- `schema/` — hand-authored JSON Schema per event + shared constants. **Single source of truth.**
- `py/generated/` — generated pydantic models + constants (consumed by `apps/api` and `packages/domain`).
- `ts/generated/` — generated TypeScript types + zod validators (consumed by `apps/web`).

Run `pnpm codegen` (root) to regenerate `py/` and `ts/` from `schema/`. Never edit generated files by hand. The codegen pipeline itself is implemented in SHARED-001.
