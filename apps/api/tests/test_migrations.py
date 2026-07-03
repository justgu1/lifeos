from __future__ import annotations

from pathlib import Path

from alembic import command
from alembic.config import Config
from sqlalchemy import create_engine, inspect


def _config(tmp_path) -> Config:
    alembic_dir = Path(__file__).resolve().parents[1] / "alembic"
    cfg = Config()
    cfg.set_main_option("script_location", str(alembic_dir))
    cfg.set_main_option("sqlalchemy.url", f"sqlite:///{tmp_path}/m.db")
    return cfg


def test_migrations_upgrade_and_downgrade(tmp_path) -> None:
    cfg = _config(tmp_path)
    command.upgrade(cfg, "head")

    engine = create_engine(f"sqlite:///{tmp_path}/m.db")
    tables = set(inspect(engine).get_table_names())
    assert {"events", "snapshots", "outbox", "config"}.issubset(tables)
    engine.dispose()

    command.downgrade(cfg, "base")
    engine = create_engine(f"sqlite:///{tmp_path}/m.db")
    remaining = set(inspect(engine).get_table_names())
    assert "events" not in remaining
    engine.dispose()
