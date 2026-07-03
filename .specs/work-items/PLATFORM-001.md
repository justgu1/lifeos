---
item: bootstrap-monorepo-and-ci
module: platform
status: active
priority: high
depends_on: []
---

# CHANGE

Bootstrap the monorepo scaffold and the CI pipeline: create apps/api, apps/web, packages/domain, packages/shared, infra/docker with base tooling (uv + pnpm workspaces), and the GitHub Actions workflows enforcing unit tests, end-to-end tests and Capacitor APK build.

## WHY

The whole project needs a solid, reproducible base before any domain code. Per ADR-006, every work-item is one PR gated by CI; this item produces that gate and the empty structure the later items fill.

## SCOPE

### Included

- root uv workspace (pyproject.toml) and pnpm workspace (pnpm-workspace.yaml, package.json)
- empty apps/api (FastAPI layout: api/application/infrastructure) with pyproject and alembic scaffold
- empty apps/web (React + Vite + TS + Capacitor + Tailwind + shadcn config)
- packages/domain (Python pure) and packages/shared (schema/py/ts) skeletons
- infra/docker (Dockerfiles + docker-compose)
- .github/workflows/ci.yml (lint, unit, e2e, import-linter) and apk.yml (APK build)
- .editorconfig, .gitignore, .env.example

### Excluded

- any domain logic, aggregates, services, endpoints, screens
- event store implementation (PLATFORM-002)

## ACCEPTANCE

### AC-001

Given a clean checkout

When a developer installs dependencies

Then uv sync and pnpm install both succeed for their respective workspaces.

### AC-002

Given a pull request

When CI runs

Then the unit, e2e and apk-build jobs are defined and execute (green on the empty scaffold).

## NOTES

The domain lives in Python (ADR-002); packages/shared holds the JSON Schema source and generated pydantic/zod outputs. No TS domain mirror.
