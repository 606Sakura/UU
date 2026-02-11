"""Run all available simulation demos."""

from pathlib import Path

from probability_sim import (
    BirthdayParadoxSimulator,
    DiceSumSimulator,
    LotterySimulator,
    MonteCarloPiEstimator,
    plot_dice_distribution,
    plot_scalar_comparison,
)


def main() -> None:
    pi_estimator = MonteCarloPiEstimator(points=100_000, seed=42)
    pi_value = pi_estimator.estimate()
    print(f"Monte Carlo π estimate: {pi_value:.6f}")

    birthday = BirthdayParadoxSimulator(people=23, trials=20_000, seed=42)
    birthday_value = birthday.estimate()
    print(f"Birthday paradox P(collision): {birthday_value:.4f}")

    dice = DiceSumSimulator(dice=2, sides=6, trials=20_000, seed=42)
    distribution = dice.distribution()
    peak_sum = max(distribution, key=distribution.get)
    print(f"2d6 most likely sum: {peak_sum} ({distribution[peak_sum]:.4f})")

    lottery = LotterySimulator(success_rate=0.02, pity=90, trials=100_000, seed=42)
    lottery_value = lottery.estimate_success_rate()
    print(f"Lottery effective success rate: {lottery_value:.4f}")

    artifacts_dir = Path("artifacts")
    artifacts_dir.mkdir(exist_ok=True)

    try:
        dice_fig = plot_dice_distribution(distribution)
        dice_path = artifacts_dir / "dice_distribution.png"
        dice_fig.savefig(dice_path, dpi=120)
        print(f"Saved chart: {dice_path}")

        compare_fig = plot_scalar_comparison(
            ["Pi/4", "Birthday", "Lottery"],
            [pi_value / 4, birthday_value, lottery_value],
            title="Simulation Metrics Comparison",
        )
        compare_path = artifacts_dir / "metrics_comparison.png"
        compare_fig.savefig(compare_path, dpi=120)
        print(f"Saved chart: {compare_path}")
    except RuntimeError as exc:
        print(f"Visualization skipped: {exc}")


if __name__ == "__main__":
    main()
