"""Validates that codegen produced importable, correct pydantic models.

Requires `scripts/codegen_py.sh` to have run (CI runs it before pytest).
"""

import pytest

pytest.importorskip(
    "lifeos_shared.generated.goal_created_schema",
    reason="run scripts/codegen_py.sh to generate models",
)


def test_goal_created_valid() -> None:
    from lifeos_shared.generated.goal_created_schema import GoalCreated

    model = GoalCreated(
        id="00000000-0000-0000-0000-000000000001",
        vision_id="00000000-0000-0000-0000-000000000002",
        title="Ship LifeOS",
        created_at="2026-07-03T12:00:00Z",
    )
    assert model.title == "Ship LifeOS"


def test_goal_created_rejects_extra() -> None:
    from pydantic import ValidationError

    from lifeos_shared.generated.goal_created_schema import GoalCreated

    with pytest.raises(ValidationError):
        GoalCreated(
            id="00000000-0000-0000-0000-000000000001",
            vision_id="00000000-0000-0000-0000-000000000002",
            title="x",
            created_at="2026-07-03T12:00:00Z",
            unexpected="nope",
        )


def test_score_shape_in_week_reviewed() -> None:
    from lifeos_shared.generated.week_reviewed_schema import WeekReviewed

    wr = WeekReviewed(
        week_id="00000000-0000-0000-0000-000000000003",
        score={"points": 6, "max_points": 10, "percentage": 60},
        reviewed_at="2026-07-05T20:00:00Z",
    )
    assert wr.score.percentage == 60
