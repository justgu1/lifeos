# CHANGELOG

> Product evolution timeline.
> Updated after every relevant change.

## [0.1.2] - 2026-07-03

### Added
- SHARED-001: canonical event schema (16 events as JSON Schema, single source of truth) with codegen to TypeScript zod validators (packages/shared/ts) and pydantic models (packages/shared/py, package lifeos-shared).
- shared-kernel value objects Progress and Score (packages/domain) with clamping and derived percentage, plus unit tests.
- CI now generates and typechecks the shared contract on both sides (zod in the web job, pydantic in the api job).

## [0.1.1] - 2026-07-03

### Fixed
- CI now runs isolated inside containers (uv image for api; Playwright image for web) and passes on the scaffold; added an images job that builds the api/web Docker images and smoke-tests the API container.
- Committed lockfiles (uv.lock, pnpm-lock.yaml) for reproducible frozen installs; ruff isort first-party config and import-linter include_external_packages; scoped vitest to src so it no longer collides with Playwright e2e; root .dockerignore (build context is the repo root).

### Changed
- APK build gate deferred to a manual workflow until PLATFORM-004 scaffolds the Capacitor Android shell (there is no Android project on the empty scaffold).

### Added
- Work-item PLATFORM-004 (android-shell-and-apk-gate).

## [0.1.0] - 2026-07-03

### Added
- Spec harness: CONTEXT.md filled (stack, ADR-001..006, glossary) and INDEX.md registering 10 modules.
- Domain modules: shared-kernel, platform, strategy, routine, planning, check-in, review, notifications, setup, ai-coach (spec, rules, checklists, contracts).
- Work-item backlog for sprints S1..S5 (PLATFORM-001 active; others draft) with dependency graph.
- Monorepo scaffold: apps/api (FastAPI), apps/web (React/Vite/Capacitor), packages/domain (pure Python), packages/shared (event schema + codegen), infra/docker.
- CI pipeline (.github/workflows): unit + e2e (ci.yml) and Capacitor APK build (apk.yml), enforcing one-work-item-one-PR.

## Format

```text
## [version] - YYYY-MM-DD

### Added
- new feature

### Changed
- behavior change

### Fixed
- bug fix

### Removed
- removed feature

### Security
- security improvement
```
