"""Monte Carlo π estimator."""

from __future__ import annotations

from dataclasses import dataclass
from random import Random


@dataclass
class MonteCarloPiEstimator:
    """Estimate π by sampling random points in the unit square."""

    points: int = 100_000
    seed: int | None = None

    def estimate(self) -> float:
        """Return a Monte Carlo estimate of π."""
        if self.points <= 0:
            raise ValueError("points must be a positive integer")

        rng = Random(self.seed)
        inside_circle = 0
        for _ in range(self.points):
            x = rng.random()
            y = rng.random()
            if x * x + y * y <= 1.0:
                inside_circle += 1

        return 4.0 * inside_circle / self.points
