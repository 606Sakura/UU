"""Birthday paradox simulation utilities."""

from __future__ import annotations

from dataclasses import dataclass
from random import Random


@dataclass
class BirthdayParadoxSimulator:
    """Simulate the probability that at least two people share a birthday."""

    people: int = 23
    trials: int = 10_000
    days_in_year: int = 365
    seed: int | None = None

    def estimate(self) -> float:
        """Return simulated collision probability for the configured group size."""
        if self.people <= 1:
            raise ValueError("people must be greater than 1")
        if self.trials <= 0:
            raise ValueError("trials must be a positive integer")
        if self.days_in_year <= 1:
            raise ValueError("days_in_year must be greater than 1")

        rng = Random(self.seed)
        collision_count = 0

        for _ in range(self.trials):
            seen = set()
            has_collision = False
            for _ in range(self.people):
                birthday = rng.randint(1, self.days_in_year)
                if birthday in seen:
                    has_collision = True
                    break
                seen.add(birthday)

            if has_collision:
                collision_count += 1

        return collision_count / self.trials
