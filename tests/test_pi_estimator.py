import unittest

from probability_sim import MonteCarloPiEstimator


class MonteCarloPiEstimatorTest(unittest.TestCase):
    def test_estimate_is_close_to_pi(self) -> None:
        estimator = MonteCarloPiEstimator(points=200_000, seed=123)
        pi_estimate = estimator.estimate()
        self.assertTrue(3.10 <= pi_estimate <= 3.18)

    def test_invalid_points_raises(self) -> None:
        estimator = MonteCarloPiEstimator(points=0)
        with self.assertRaises(ValueError):
            estimator.estimate()


if __name__ == "__main__":
    unittest.main()
