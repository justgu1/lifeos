"""Alembic environment.

Scaffold only. Target metadata is wired to the SQLAlchemy models in
PLATFORM-002 (events, snapshots, outbox, config).
"""

from alembic import context

target_metadata = None


def run_migrations_offline() -> None:
    context.configure(url=context.config.get_main_option("sqlalchemy.url"))
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    # Engine/connection wiring added in PLATFORM-002.
    raise NotImplementedError("online migrations wired in PLATFORM-002")


if context.is_offline_mode():
    run_migrations_offline()
