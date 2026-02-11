"""Generic lottery / probability event simulation."""

from __future__ import annotations

from dataclasses import dataclass
from random import Random


@dataclass
class LotterySimulator:
    """Simulate Bernoulli trials with optional pity guarantee."""

    success_rate: float
    trials: int = 10_000
    pity: int | None = None
    seed: int | None = None

    def estimate_success_rate(self) -> float:
        """Return empirical success probability per pull."""
        if not 0.0 < self.success_rate <= 1.0:
            raise ValueError("success_rate must be in (0, 1]")
        if self.trials <= 0:
            raise ValueError("trials must be a positive integer")
        if self.pity is not None and self.pity <= 0:
            raise ValueError("pity must be a positive integer when provided")

        rng = Random(self.seed)
        successes = 0
        failures_since_success = 0

        for _ in range(self.trials):
            forced_success = self.pity is not None and failures_since_success >= self.pity - 1
            if forced_success or rng.random() < self.success_rate:
                successes += 1
                failures_since_success = 0
            else:
                failures_since_success += 1

        return successes / self.trials
