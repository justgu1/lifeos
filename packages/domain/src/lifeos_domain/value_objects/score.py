"""Score value object — points achieved vs possible, with derived percentage."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True, slots=True)
class Score:
    """Immutable, equality-by-value.

    Invariant: ``points <= max_points``. ``percentage`` is derived
    (0 when ``max_points`` is 0).
    """

    points: int
    max_points: int
    percentage: int = field(default=0)

    def __post_init__(self) -> None:
        if self.points < 0 or self.max_points < 0:
            raise ValueError("Score points and max_points must be non-negative")
        if self.points > self.max_points:
            raise ValueError("Score points cannot exceed max_points")
        pct = round(self.points / self.max_points * 100) if self.max_points > 0 else 0
        object.__setattr__(self, "percentage", pct)

    @classmethod
    def of(cls, points: int, max_points: int) -> Score:
        return cls(points=points, max_points=max_points)

    def add(self, points: int, max_points: int) -> Score:
        """Return a new Score with the given points/max_points accumulated."""
        return Score.of(self.points + points, self.max_points + max_points)
