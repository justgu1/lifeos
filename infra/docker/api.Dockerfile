# LifeOS API image (scaffold)
FROM python:3.12-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app
COPY pyproject.toml uv.lock ./
COPY packages/domain ./packages/domain
COPY packages/shared/py ./packages/shared/py
COPY packages/shared/schema ./packages/shared/schema
COPY scripts ./scripts
COPY apps/api ./apps/api

RUN uv sync --package lifeos-api --frozen --no-dev || uv sync --package lifeos-api
# Generate pydantic event models from the shared JSON Schema (payload validation).
RUN bash scripts/codegen_py.sh

COPY infra/docker/api-entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh && mkdir -p /app/data

ENV LIFEOS_DATABASE_URL=sqlite:////app/data/lifeos.db

EXPOSE 8000
CMD ["sh", "/app/entrypoint.sh"]
