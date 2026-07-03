"""FastAPI application factory."""

from __future__ import annotations

from fastapi import FastAPI

from app.api.routes import events


def create_app() -> FastAPI:
    app = FastAPI(title="LifeOS API", version="0.1.0")

    @app.get("/health")
    def health() -> dict[str, str]:
        return {"status": "ok"}

    app.include_router(events.router)
    return app


app = create_app()
