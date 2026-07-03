"""Alembic environment wired to the SQLAlchemy models."""

from __future__ import annotations

import os

from alembic import context
from sqlalchemy import engine_from_config, pool

import app.infrastructure.models  # noqa: F401 - register tables on metadata
from app.infrastructure.db.base import Base

config = context.config
target_metadata = Base.metadata

# Prefer the runtime database URL so migrations and the app share one database.
_db_url = os.environ.get("LIFEOS_DATABASE_URL")
if _db_url:
    config.set_main_option("sqlalchemy.url", _db_url)


def run_migrations_offline() -> None:
    context.configure(
        url=config.get_main_option("sqlalchemy.url"),
        target_metadata=target_metadata,
        literal_binds=True,
        render_as_batch=True,
    )
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    section = config.get_section(config.config_ini_section) or {}
    connectable = engine_from_config(section, prefix="sqlalchemy.", poolclass=pool.NullPool)
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            render_as_batch=True,
        )
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
