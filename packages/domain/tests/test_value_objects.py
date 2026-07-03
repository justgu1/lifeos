from dataclasses import FrozenInstanceError

import pytest

from lifeos_domain.value_objects import Progress, Score


class TestProgress:
    def test_clamped_high(self) -> None:
        assert Progress(value=150).value == 100

    def test_clamped_low(self) -> None:
        assert Progress(value=-10).value == 0

    def test_from_counts(self) -> None:
        p = Progress.from_counts(1, 4)
        assert p.value == 25
        assert p.source_count == 4

    def test_from_counts_zero_total(self) -> None:
        p = Progress.from_counts(0, 0)
        assert p.value == 0
        assert p.source_count == 0

    def test_equality_by_value(self) -> None:
        assert Progress(50, 2) == Progress(50, 2)

    def test_immutable(self) -> None:
        with pytest.raises(FrozenInstanceError):
            Progress(50).value = 60  # type: ignore[misc]


class TestScore:
    def test_percentage(self) -> None:
        assert Score.of(3, 4).percentage == 75

    def test_max_points_zero(self) -> None:
        assert Score.of(0, 0).percentage == 0

    def test_full(self) -> None:
        assert Score.of(10, 10).percentage == 100

    def test_points_exceed_raises(self) -> None:
        with pytest.raises(ValueError):
            Score.of(5, 4)

    def test_negative_raises(self) -> None:
        with pytest.raises(ValueError):
            Score.of(-1, 4)

    def test_add(self) -> None:
        s = Score.of(1, 2).add(2, 2)
        assert s.points == 3
        assert s.max_points == 4
        assert s.percentage == 75
