#!/usr/bin/env sh
# Apply migrations, then start the API. DB path comes from LIFEOS_DATABASE_URL.
set -e
cd /app/apps/api
uv run alembic upgrade head
exec uv run uvicorn app.main:app --host 0.0.0.0 --port 8000
