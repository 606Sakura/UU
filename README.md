# Probability Simulation Toolkit

一个轻量的 Python 概率模拟工具包，适合教学、学习和实验。

## 当前功能
- 蒙特卡洛方法估算 `π`
- 生日悖论概率模拟
- 多骰子点数和分布模拟
- 通用抽奖/概率事件模拟（支持保底机制）
- 图表可视化（若安装 matplotlib）

## 安装
```bash
pip install -r requirements.txt
# 或安装为包
pip install .
```

> 可视化依赖 `matplotlib`，按需安装：
```bash
pip install matplotlib
```

## 快速开始
```python
from probability_sim import MonteCarloPiEstimator

sim = MonteCarloPiEstimator(points=100_000, seed=42)
pi_estimate = sim.estimate()
print(f"估算 π: {pi_estimate:.6f}")
```

## 运行完整示例
```bash
PYTHONPATH=src python examples/run_all.py
```

运行后会在 `artifacts/` 下输出图表文件（若 matplotlib 可用）：
- `dice_distribution.png`
- `metrics_comparison.png`

## 核心 API
- `MonteCarloPiEstimator(points=100_000, seed=None).estimate() -> float`
- `BirthdayParadoxSimulator(people=23, trials=10_000, days_in_year=365, seed=None).estimate() -> float`
- `DiceSumSimulator(dice=2, sides=6, trials=10_000, seed=None).distribution() -> dict[int, float]`
- `LotterySimulator(success_rate, trials=10_000, pity=None, seed=None).estimate_success_rate() -> float`
- `plot_dice_distribution(distribution) -> Figure`
- `plot_scalar_comparison(labels, values, title) -> Figure`
