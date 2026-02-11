import unittest

from probability_sim import BirthdayParadoxSimulator


class BirthdayParadoxSimulatorTest(unittest.TestCase):
    def test_probability_is_reasonable_for_23_people(self) -> None:
        simulator = BirthdayParadoxSimulator(people=23, trials=50_000, seed=7)
        probability = simulator.estimate()
        self.assertTrue(0.45 <= probability <= 0.55)

    def test_invalid_people_raises(self) -> None:
        simulator = BirthdayParadoxSimulator(people=1)
        with self.assertRaises(ValueError):
            simulator.estimate()


if __name__ == "__main__":
    unittest.main()
