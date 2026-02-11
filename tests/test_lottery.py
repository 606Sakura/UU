import unittest

from probability_sim import LotterySimulator


class LotterySimulatorTest(unittest.TestCase):
    def test_pity_increases_effective_rate(self) -> None:
        no_pity = LotterySimulator(success_rate=0.01, pity=None, trials=200_000, seed=1)
        with_pity = LotterySimulator(success_rate=0.01, pity=90, trials=200_000, seed=1)

        self.assertGreater(with_pity.estimate_success_rate(), no_pity.estimate_success_rate())

    def test_invalid_rate_raises(self) -> None:
        simulator = LotterySimulator(success_rate=0.0)
        with self.assertRaises(ValueError):
            simulator.estimate_success_rate()


if __name__ == "__main__":
    unittest.main()
