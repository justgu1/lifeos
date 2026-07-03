"""FastAPI application factory.

Scaffold only — no routes wired yet. Endpoints (POST /events, GET /week,
GET /today, GET /dashboard, POST /review, POST /setup) are added by their
respective work-items once activated.
"""

from fastapi import FastAPI


def create_app() -> FastAPI:
    app = FastAPI(title="LifeOS API", version="0.1.0")

    @app.get("/health")
    def health() -> dict[str, str]:
        return {"status": "ok"}

    return app


app = create_app()
