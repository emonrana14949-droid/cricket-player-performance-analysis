"""Analyse the cricket batting dataset with Pandas, NumPy and Matplotlib.

Run from the project root:
    python src/analysis.py

Outputs are saved to:
    outputs/tables/  (CSV summary tables)
    outputs/charts/  (PNG visualizations)
    outputs/insights.md
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "cricket_performance_dataset.csv"
TABLE_DIR = PROJECT_ROOT / "outputs" / "tables"
CHART_DIR = PROJECT_ROOT / "outputs" / "charts"
INSIGHTS_PATH = PROJECT_ROOT / "outputs" / "insights.md"

try:
    plt.style.use("seaborn-v0_8-whitegrid")
except OSError:
    plt.style.use("ggplot")


def save_bar_chart(series: pd.Series, title: str, xlabel: str, ylabel: str, path: Path) -> None:
    fig, ax = plt.subplots(figsize=(9, 4.8))
    series.plot(kind="bar", ax=ax, color="#2f81f7", edgecolor="white")
    ax.set_title(title, fontweight="bold")
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.tick_params(axis="x", rotation=25)
    for label in ax.get_xticklabels():
        label.set_ha("right")
    fig.tight_layout()
    fig.savefig(path, dpi=160)
    plt.close(fig)


def main() -> None:
    TABLE_DIR.mkdir(parents=True, exist_ok=True)
    CHART_DIR.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(DATA_PATH)

    # Basic cleaning.
    df = df.drop_duplicates().copy()
    numeric_cols = ["runs", "balls_faced", "fours", "sixes", "strike_rate"]
    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors="coerce")
    df = df.dropna(subset=numeric_cols)
    df["times_out"] = np.where(df["dismissal"] == "Out", 1, 0)
    df["is_fifty"] = np.where((df["runs"] >= 50) & (df["runs"] < 100), 1, 0)
    df["is_hundred"] = np.where(df["runs"] >= 100, 1, 0)

    # Summary tables.
    df.describe(include="all").round(2).to_csv(TABLE_DIR / "summary_statistics.csv")

    player_summary = (
        df.groupby("player")
        .agg(
            innings=("match_id", "count"),
            total_runs=("runs", "sum"),
            times_out=("times_out", "sum"),
            avg_strike_rate=("strike_rate", "mean"),
            fifties=("is_fifty", "sum"),
            hundreds=("is_hundred", "sum"),
            highest_score=("runs", "max"),
        )
        .reset_index()
    )
    player_summary["batting_average"] = (
        player_summary["total_runs"] / player_summary["times_out"]
    )
    player_summary = player_summary.round(2).sort_values(
        "batting_average", ascending=False
    )
    player_summary.to_csv(TABLE_DIR / "player_summary.csv", index=False)

    by_opponent = (
        df.groupby("opponent")
        .agg(
            innings=("match_id", "count"),
            total_runs=("runs", "sum"),
            avg_runs=("runs", "mean"),
            avg_strike_rate=("strike_rate", "mean"),
        )
        .round(2)
        .sort_values("avg_runs", ascending=False)
    )
    by_opponent.to_csv(TABLE_DIR / "performance_by_opponent.csv")

    corr = df[["runs", "balls_faced", "fours", "sixes", "strike_rate"]].corr(
        numeric_only=True
    ).round(2)
    corr.to_csv(TABLE_DIR / "correlation_matrix.csv")

    # Chart 1: batting average by player.
    save_bar_chart(
        player_summary.set_index("player")["batting_average"],
        "Batting Average by Player",
        "Player",
        "Batting average",
        CHART_DIR / "average_runs_by_player.png",
    )

    # Chart 2: strike rate vs runs scatter.
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.scatter(df["runs"], df["strike_rate"], alpha=0.65, color="#2f81f7", edgecolor="white", linewidth=0.4)
    ax.set_title("Strike Rate vs Runs", fontweight="bold")
    ax.set_xlabel("Runs scored")
    ax.set_ylabel("Strike rate")
    fig.tight_layout()
    fig.savefig(CHART_DIR / "strike_rate_vs_runs.png", dpi=160)
    plt.close(fig)

    # Chart 3: runs distribution with mean line.
    fig, ax = plt.subplots(figsize=(9, 4.8))
    ax.hist(df["runs"], bins=18, color="#8250df", edgecolor="white")
    ax.axvline(df["runs"].mean(), color="#111111", linestyle="--", linewidth=1.5, label="Mean")
    ax.set_title("Distribution of Runs per Innings", fontweight="bold")
    ax.set_xlabel("Runs")
    ax.set_ylabel("Number of innings")
    ax.legend()
    fig.tight_layout()
    fig.savefig(CHART_DIR / "runs_distribution.png", dpi=160)
    plt.close(fig)

    # Chart 4: average runs by opponent.
    save_bar_chart(
        by_opponent["avg_runs"],
        "Average Runs by Opponent",
        "Opponent",
        "Average runs per innings",
        CHART_DIR / "average_runs_by_opponent.png",
    )

    # Key findings for insights.md.
    best_avg = player_summary.iloc[0]
    regulars = player_summary[player_summary["innings"] >= 30]
    best_sr = regulars.loc[regulars["avg_strike_rate"].idxmax()]
    most_hundreds = player_summary.loc[player_summary["hundreds"].idxmax()]
    top_scorer = player_summary.loc[player_summary["total_runs"].idxmax()]

    insights = f"""# Key Insights — Cricket Player Performance Analysis

> This project uses synthetic practice data generated with NumPy. The player names are real Bangladesh cricketers, but all numbers are made up for practice — they are not real match statistics.

- Dataset size: **{len(df)} innings** across **{df['player'].nunique()} players**.
- Highest batting average: **{best_avg['player']}** ({best_avg['batting_average']:.2f}).
- Highest average strike rate (players with 30+ innings): **{best_sr['player']}** ({best_sr['avg_strike_rate']:.2f}).
- Most centuries: **{most_hundreds['player']}** ({int(most_hundreds['hundreds'])} {'century' if int(most_hundreds['hundreds']) == 1 else 'hundreds'}).
- Most total runs: **{top_scorer['player']}** ({int(top_scorer['total_runs'])} runs in {int(top_scorer['innings'])} innings).
- Best opponent to bat against (highest average runs): **{by_opponent.index[0]}** ({by_opponent.iloc[0]['avg_runs']:.2f} average runs per innings).

## Charts

- `charts/average_runs_by_player.png`
- `charts/strike_rate_vs_runs.png`
- `charts/runs_distribution.png`
- `charts/average_runs_by_opponent.png`

## Important note

These patterns come from randomly generated practice data. For a real project, replace the synthetic CSV with real scorecard data and document the source and coverage.
"""
    INSIGHTS_PATH.write_text(insights, encoding="utf-8")

    print("Analysis complete.")
    print(f"Tables saved to: {TABLE_DIR}")
    print(f"Charts saved to: {CHART_DIR}")
    print(f"Insights saved to: {INSIGHTS_PATH}")
    print(f"Highest batting average: {best_avg['player']} ({best_avg['batting_average']:.2f})")
    print(f"Most centuries: {most_hundreds['player']} ({int(most_hundreds['hundreds'])})")


if __name__ == "__main__":
    main()
