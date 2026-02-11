"""Visualization utilities for simulation results."""

from __future__ import annotations

from typing import Iterable


def _require_matplotlib():
    try:
        import matplotlib.pyplot as plt
    except ModuleNotFoundError as exc:
        raise RuntimeError(
            "matplotlib is required for visualization. Install it with `pip install matplotlib`."
        ) from exc
    return plt


def plot_dice_distribution(distribution: dict[int, float], title: str = "Dice Sum Distribution"):
    """Create a bar chart for dice sum probabilities."""
    if not distribution:
        raise ValueError("distribution cannot be empty")

    plt = _require_matplotlib()
    sums = list(distribution.keys())
    probs = list(distribution.values())

    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.bar(sums, probs)
    ax.set_title(title)
    ax.set_xlabel("Sum")
    ax.set_ylabel("Probability")
    ax.grid(alpha=0.2)
    fig.tight_layout()
    return fig


def plot_scalar_comparison(labels: Iterable[str], values: Iterable[float], title: str):
    """Create a simple bar chart for scalar metric comparisons."""
    labels = list(labels)
    values = list(values)
    if len(labels) == 0 or len(labels) != len(values):
        raise ValueError("labels and values must be non-empty and have the same length")

    plt = _require_matplotlib()
    fig, ax = plt.subplots(figsize=(7, 4.2))
    ax.bar(labels, values)
    ax.set_title(title)
    ax.set_ylabel("Value")
    ax.grid(axis="y", alpha=0.2)
    fig.tight_layout()
    return fig
