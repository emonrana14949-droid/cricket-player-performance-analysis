"""Generate a synthetic cricket batting dataset for practice.

The player names are real Bangladesh cricketers, but every number in this
dataset is made up for Data Science practice only. It is not real match data.
"""

from pathlib import Path

import numpy as np
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "cricket_performance_dataset.csv"

# Player skill profiles: (mean runs per innings, strike-rate tendency)
PLAYER_PROFILES = {
    "Tamim Iqbal": (38, 82),
    "Shakib Al Hasan": (36, 88),
    "Mushfiqur Rahim": (37, 84),
    "Litton Das": (34, 95),
    "Najmul Hossain Shanto": (35, 85),
    "Towhid Hridoy": (32, 90),
    "Mahmudullah": (30, 80),
}

OPPONENTS = [
    "India",
    "Pakistan",
    "Sri Lanka",
    "Australia",
    "England",
    "New Zealand",
    "Afghanistan",
    "West Indies",
]
VENUES = ["Home", "Away", "Neutral"]


def main() -> None:
    rng = np.random.default_rng(42)
    n = 360

    players = list(PLAYER_PROFILES.keys())
    player = rng.choice(players, size=n)
    opponent = rng.choice(OPPONENTS, size=n)
    venue = rng.choice(VENUES, size=n, p=[0.45, 0.35, 0.20])

    mean_runs = np.array([PLAYER_PROFILES[p][0] for p in player], dtype=float)
    sr_tendency = np.array([PLAYER_PROFILES[p][1] for p in player], dtype=float)

    runs = np.clip(rng.normal(mean_runs, 22), 0, 160).round().astype(int)

    # Balls faced derived from runs and the player's strike-rate tendency.
    effective_sr = np.clip(rng.normal(sr_tendency, 12), 40, 180)
    balls_faced = np.where(
        runs > 0,
        np.maximum(1, np.round(runs / (effective_sr / 100) + rng.normal(0, 3, size=n))),
        rng.integers(1, 9, size=n),
    ).astype(int)
    balls_faced = np.maximum(balls_faced, 1)

    # Fours and sixes derived plausibly from runs (boundary runs stay <= runs).
    boundary_share = rng.uniform(0.30, 0.65, size=n) * runs
    sixes = (boundary_share * rng.uniform(0.2, 0.5, size=n) // 6).astype(int)
    fours = ((boundary_share - sixes * 6) // 4).astype(int)
    over = 4 * fours + 6 * sixes - runs
    fours = np.where(over > 0, np.maximum(0, fours - np.ceil(over / 4).astype(int)), fours)

    dismissal = np.where(rng.random(n) < 0.15, "Not Out", "Out")
    strike_rate = np.round(runs / balls_faced * 100, 2)
    match_result = rng.choice(["Won", "Lost"], size=n, p=[0.5, 0.5])

    df = pd.DataFrame(
        {
            "match_id": [f"M-{i:03d}" for i in range(1, n + 1)],
            "player": player,
            "opponent": opponent,
            "venue": venue,
            "runs": runs,
            "balls_faced": balls_faced,
            "fours": fours,
            "sixes": sixes,
            "dismissal": dismissal,
            "strike_rate": strike_rate,
            "match_result": match_result,
        }
    )

    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(DATA_PATH, index=False)
    print(f"Dataset created: {DATA_PATH}")
    print(f"Rows: {len(df)} | Columns: {len(df.columns)}")


if __name__ == "__main__":
    main()
