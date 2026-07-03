# CHANGELOG

> Product evolution timeline.
> Updated after every relevant change.

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
