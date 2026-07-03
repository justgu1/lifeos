"""Progress value object — normalized 0..100 completion measure."""

from __future__ import annotations

from dataclasses import dataclass

MIN_PROGRESS = 0
MAX_PROGRESS = 100


@dataclass(frozen=True, slots=True)
class Progress:
    """Immutable, equality-by-value. `value` is always clamped to 0..100."""

    value: int
    source_count: int = 0

    def __post_init__(self) -> None:
        clamped = max(MIN_PROGRESS, min(MAX_PROGRESS, self.value))
        object.__setattr__(self, "value", clamped)
        if self.source_count < 0:
            object.__setattr__(self, "source_count", 0)

    @classmethod
    def from_counts(cls, completed: int, total: int) -> Progress:
        """Build Progress from completed/total, guarding division by zero."""
        if total <= 0:
            return cls(value=0, source_count=0)
        ratio = round(completed / total * MAX_PROGRESS)
        return cls(value=ratio, source_count=total)
