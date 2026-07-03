# LifeOS API image (scaffold)
FROM python:3.12-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app
COPY pyproject.toml uv.lock ./
COPY packages/domain ./packages/domain
COPY apps/api ./apps/api

RUN uv sync --package lifeos-api --frozen --no-dev || uv sync --package lifeos-api

EXPOSE 8000
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
