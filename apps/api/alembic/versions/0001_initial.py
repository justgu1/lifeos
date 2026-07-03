"""initial event-sourcing schema

Revision ID: 0001_initial
Revises:
Create Date: 2026-07-03
"""

from __future__ import annotations

import sqlalchemy as sa
from alembic import op

revision = "0001_initial"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "events",
        sa.Column("id", sa.String(length=26), primary_key=True),
        sa.Column("aggregate_id", sa.String(length=36), nullable=False),
        sa.Column("aggregate_type", sa.String(length=64), nullable=False),
        sa.Column("version", sa.Integer(), nullable=False),
        sa.Column("event_type", sa.String(length=64), nullable=False),
        sa.Column("schema_version", sa.Integer(), nullable=False),
        sa.Column("payload", sa.JSON(), nullable=False),
        sa.Column("created_at", sa.String(length=32), nullable=False),
        sa.UniqueConstraint("aggregate_id", "version", name="uq_events_aggregate_version"),
    )
    op.create_index("ix_events_aggregate", "events", ["aggregate_id", "version"])
    op.create_index("ix_events_type_created", "events", ["aggregate_type", "created_at"])

    op.create_table(
        "snapshots",
        sa.Column("aggregate_id", sa.String(length=36), primary_key=True),
        sa.Column("aggregate_type", sa.String(length=64), nullable=False),
        sa.Column("version", sa.Integer(), nullable=False),
        sa.Column("payload", sa.JSON(), nullable=False),
        sa.Column("created_at", sa.String(length=32), nullable=False),
    )

    op.create_table(
        "outbox",
        sa.Column("id", sa.String(length=26), primary_key=True),
        sa.Column("payload", sa.JSON(), nullable=False),
        sa.Column("status", sa.String(length=16), nullable=False),
        sa.Column("attempts", sa.Integer(), nullable=False),
        sa.Column("last_error", sa.Text(), nullable=True),
        sa.Column("created_at", sa.String(length=32), nullable=False),
        sa.Column("synced_at", sa.String(length=32), nullable=True),
    )
    op.create_index("ix_outbox_status", "outbox", ["status"])

    op.create_table(
        "config",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("timezone", sa.String(length=64), nullable=False),
        sa.Column("notification_hours", sa.JSON(), nullable=False),
        sa.Column("week_start_day", sa.String(length=16), nullable=False),
        sa.Column("cycle_length_weeks", sa.Integer(), nullable=False),
        sa.Column("flags", sa.JSON(), nullable=False),
    )


def downgrade() -> None:
    op.drop_index("ix_outbox_status", table_name="outbox")
    op.drop_table("config")
    op.drop_table("outbox")
    op.drop_index("ix_events_type_created", table_name="events")
    op.drop_index("ix_events_aggregate", table_name="events")
    op.drop_table("snapshots")
    op.drop_table("events")
