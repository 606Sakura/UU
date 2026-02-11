import unittest

from probability_sim import DiceSumSimulator


class DiceSumSimulatorTest(unittest.TestCase):
    def test_two_dice_peak_near_seven(self) -> None:
        simulator = DiceSumSimulator(dice=2, sides=6, trials=80_000, seed=9)
        distribution = simulator.distribution()
        peak = max(distribution, key=distribution.get)
        self.assertEqual(peak, 7)

    def test_distribution_probabilities_sum_to_one(self) -> None:
        simulator = DiceSumSimulator(dice=3, sides=6, trials=10_000, seed=5)
        distribution = simulator.distribution()
        total = sum(distribution.values())
        self.assertTrue(0.99 <= total <= 1.01)


if __name__ == "__main__":
    unittest.main()
