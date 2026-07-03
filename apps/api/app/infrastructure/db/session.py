"""Engine/session factory. SQLite runs in WAL mode so the outbox relay can
coexist with writes (platform rule)."""

from __future__ import annotations

from collections.abc import Iterator

from sqlalchemy import Engine, create_engine, event
from sqlalchemy.orm import Session, sessionmaker

from app.config import get_settings


def _apply_sqlite_pragmas(engine: Engine) -> None:
    if not engine.url.get_backend_name().startswith("sqlite"):
        return

    @event.listens_for(engine, "connect")
    def _set_pragmas(dbapi_conn, _record) -> None:  # noqa: ANN001
        cursor = dbapi_conn.cursor()
        cursor.execute("PRAGMA journal_mode=WAL")
        cursor.execute("PRAGMA busy_timeout=5000")
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()


def create_db_engine(url: str | None = None) -> Engine:
    database_url = url or get_settings().database_url
    connect_args = {"check_same_thread": False} if database_url.startswith("sqlite") else {}
    engine = create_engine(database_url, connect_args=connect_args, future=True)
    _apply_sqlite_pragmas(engine)
    return engine


_engine: Engine | None = None
_SessionLocal: sessionmaker[Session] | None = None


def _ensure_factory() -> sessionmaker[Session]:
    global _engine, _SessionLocal
    if _SessionLocal is None:
        _engine = create_db_engine()
        _SessionLocal = sessionmaker(bind=_engine, expire_on_commit=False, future=True)
    return _SessionLocal


def get_session() -> Iterator[Session]:
    factory = _ensure_factory()
    session = factory()
    try:
        yield session
    finally:
        session.close()
