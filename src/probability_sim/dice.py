"""Dice simulation helpers."""

from __future__ import annotations

from dataclasses import dataclass
from random import Random


@dataclass
class DiceSumSimulator:
    """Simulate the sum distribution of rolling multiple fair dice."""

    dice: int = 2
    sides: int = 6
    trials: int = 10_000
    seed: int | None = None

    def distribution(self) -> dict[int, float]:
        """Return empirical probability distribution of sum outcomes."""
        if self.dice <= 0:
            raise ValueError("dice must be a positive integer")
        if self.sides <= 1:
            raise ValueError("sides must be greater than 1")
        if self.trials <= 0:
            raise ValueError("trials must be a positive integer")

        rng = Random(self.seed)
        counts: dict[int, int] = {}
        for _ in range(self.trials):
            outcome = sum(rng.randint(1, self.sides) for _ in range(self.dice))
            counts[outcome] = counts.get(outcome, 0) + 1

        return {value: count / self.trials for value, count in sorted(counts.items())}
