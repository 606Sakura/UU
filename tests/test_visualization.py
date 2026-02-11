import importlib.util
import unittest

from probability_sim import plot_dice_distribution, plot_scalar_comparison


class VisualizationTest(unittest.TestCase):
    def test_invalid_distribution_raises(self) -> None:
        with self.assertRaises(ValueError):
            plot_dice_distribution({})

    def test_invalid_scalar_input_raises(self) -> None:
        with self.assertRaises(ValueError):
            plot_scalar_comparison([], [], title="x")

    @unittest.skipIf(importlib.util.find_spec("matplotlib") is None, "matplotlib not installed")
    def test_chart_creation_returns_figure(self) -> None:
        fig = plot_dice_distribution({2: 0.1, 3: 0.2, 4: 0.3})
        self.assertTrue(hasattr(fig, "savefig"))


if __name__ == "__main__":
    unittest.main()
