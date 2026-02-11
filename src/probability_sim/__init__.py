"""Probability simulation toolkit package."""

from .birthday_paradox import BirthdayParadoxSimulator
from .dice import DiceSumSimulator
from .lottery import LotterySimulator
from .pi_estimator import MonteCarloPiEstimator
from .visualization import plot_dice_distribution, plot_scalar_comparison

__all__ = [
    "MonteCarloPiEstimator",
    "BirthdayParadoxSimulator",
    "DiceSumSimulator",
    "LotterySimulator",
    "plot_dice_distribution",
    "plot_scalar_comparison",
]
