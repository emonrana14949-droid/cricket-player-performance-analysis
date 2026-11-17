# Project Guide — Cricket Player Performance Analysis

This guide explains **everything** in this project, from the very start. It is written for beginners. Read it top to bottom and you will understand the topic, the data, every file, and the code.

---

## 1. What is this project?

This is a **Data Science practice project** about cricket batting. It takes a dataset of **360 batting innings** (one row = one innings of one player) and answers these questions:

1. Which player has the highest batting average?
2. Which player scores the fastest (highest strike rate)?
3. Who has scored the most fifties (50s) and centuries (100s)?
4. Against which opponent do batters score the most runs?
5. How are runs, balls faced, boundaries and strike rate related?

Three Python libraries do the work: **NumPy** generates the dataset with random numbers, **Pandas** cleans the data and calculates summaries, and **Matplotlib** draws the charts.

> ⚠️ **Very important:** The player names are **real Bangladesh cricketers** (Tamim Iqbal, Shakib Al Hasan, Mushfiqur Rahim, Litton Das, Najmul Hossain Shanto, Towhid Hridoy, Mahmudullah). But **every number in this project is made up** by a random number generator for practice. These are **NOT** real match statistics. Never present these numbers as a player's real career record.

---

## 2. What is inside the project?

```text
cricket-player-performance-analysis/
├── README.md
├── PROJECT_GUIDE.md
├── requirements.txt
├── .gitignore
├── data/cricket_performance_dataset.csv
├── src/generate_dataset.py
├── src/analysis.py
├── notebooks/cricket_performance_analysis.ipynb
└── outputs/ (insights.md, tables/, charts/)
```

- **README.md** — The front page of the project: short summary, the questions, project structure and quick-start commands. Read this first for an overview.
- **PROJECT_GUIDE.md** — This file: the full beginner-friendly explanation of the data, the code, the outputs, the results, and viva questions.
- **requirements.txt** — Lists the libraries the project needs: `pandas`, `numpy`, `matplotlib`. The command `pip install -r requirements.txt` installs all of them at once.
- **.gitignore** — A file for Git (version control). It tells Git which files NOT to upload to GitHub, such as `__pycache__/` folders and virtual environments. You can ignore it while learning.
- **data/cricket_performance_dataset.csv** — The dataset. CSV means "comma-separated values": a simple table you can open in Excel, Google Sheets or Python. It has 360 rows and 11 columns. It is **created by** `src/generate_dataset.py`.
- **src/generate_dataset.py** — Python code that creates the dataset: it invents 360 innings using NumPy random numbers and saves them as the CSV above. Run this first.
- **src/analysis.py** — Python code that reads the CSV, cleans it, calculates all summaries, draws all charts and writes the findings. Run this second.
- **notebooks/cricket_performance_analysis.ipynb** — A Jupyter Notebook version of the analysis. A notebook lets you run code in small pieces (cells) and see each result right below the code. Good for learning and presenting step by step.
- **outputs/tables/** — CSV summary tables made by `analysis.py`:
  - `summary_statistics.csv` — overall statistics of every column (count, mean, min, max and more).
  - `player_summary.csv` — one row per player: innings, total runs, batting average, average strike rate, 50s, 100s, highest score.
  - `performance_by_opponent.csv` — one row per opponent: average runs and average strike rate against that team.
  - `correlation_matrix.csv` — how strongly pairs of numbers move together (runs, balls faced, fours, sixes, strike rate).
- **outputs/charts/** — PNG images made by `analysis.py`: `average_runs_by_player.png` (bar chart of batting average), `strike_rate_vs_runs.png` (scatter plot of runs vs strike rate), `runs_distribution.png` (histogram of runs per innings), `average_runs_by_opponent.png` (bar chart of average runs by opponent).
- **outputs/insights.md** — A short written report of the key findings, written automatically by `analysis.py`. The fastest way to see the project's results.

---

## 3. The dataset, column by column

The dataset `data/cricket_performance_dataset.csv` has **360 rows** (innings) and **11 columns**. The first real row looks like this:

```text
M-001, Tamim Iqbal, Afghanistan, Neutral, 45, 66, 3, 0, Not Out, 68.18, Lost
```

| Column | What it means | Example values |
|---|---|---|
| `match_id` | A simple ID for the row. | `M-001`, `M-002` |
| `player` | The batter who played this innings. One of 7 Bangladesh players. | `Tamim Iqbal`, `Litton Das` |
| `opponent` | The team played against. One of 8 teams. | `India`, `Pakistan`, `Afghanistan` |
| `venue` | Where the match was played: `Home` (in Bangladesh), `Away` (opponent's country) or `Neutral` (a third country). | `Home`, `Away`, `Neutral` |
| `runs` | Runs scored in this innings. Can be 0 to 160. | `45`, `27`, `102` |
| `balls_faced` | Balls the player faced. Always at least 1. | `66`, `38` |
| `fours` | Boundaries worth 4 runs hit in this innings. | `3`, `0`, `11` |
| `sixes` | Boundaries worth 6 runs hit in this innings. | `0`, `2` |
| `dismissal` | `Out` = the player got out. `Not Out` = the innings/match ended while he was still batting. | `Out`, `Not Out` |
| `strike_rate` | How fast the player scored. Formula below. | `68.18`, `71.05` |
| `match_result` | Did the player's team win this match? | `Won`, `Lost` |

### How is strike rate calculated?

```text
strike rate = runs / balls faced × 100
```

Example from row 1: Tamim Iqbal scored 45 runs from 66 balls → 45 / 66 × 100 = **68.18**. A strike rate of 100 means exactly 1 run per ball on average. Higher = faster scoring.

### How is batting average calculated?

Batting average is **not** in the CSV. The analysis code calculates it per player:

```text
batting average = total runs / times out
```

"Times out" counts only the innings where the player got `Out`. A `Not Out` innings does **not** count in the denominator. Example: 500 total runs and 10 times out → average = 500 / 10 = **50.00**. This is the standard cricket definition: it rewards players who score runs **and** stay not out.

---

## 4. How to run the project from zero

**Step 1 — Install Python.** Install Python 3 from [python.org](https://www.python.org/downloads/). On Windows, tick **"Add Python to PATH"**. Check it works:

```bash
python --version
```

**Step 2 — Open the project folder in a terminal:**

```bash
cd cricket-player-performance-analysis
```

**Step 3 — Install the libraries:**

```bash
pip install -r requirements.txt
```

**Step 4 — Generate the dataset:**

```bash
python src/generate_dataset.py
```

You should see: `Dataset created: .../data/cricket_performance_dataset.csv` and `Rows: 360 | Columns: 11`.

**Step 5 — Run the analysis:**

```bash
python src/analysis.py
```

You should see "Analysis complete." plus the top findings.

**Step 6 — See the outputs.** Read `outputs/insights.md` for the findings, open the PNG files in `outputs/charts/` for the pictures, open the CSVs in `outputs/tables/` for the numbers (they open nicely in Excel or Google Sheets), or open `notebooks/cricket_performance_analysis.ipynb` in Jupyter/VS Code and run the cells one by one.

> Tip: you can run Step 4 again any time. Because the random seed is fixed (see §5.3), you get the **same dataset** every time.

---

## 5. Code explanation: `src/generate_dataset.py`

This file **creates** the data. We walk through it in order.

### 5.1 Imports and file paths

```python
from pathlib import Path
import numpy as np
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "cricket_performance_dataset.csv"
```

`numpy` (short name `np`) is used for random numbers and maths; `pandas` (`pd`) builds the table and saves it. `Path(__file__).resolve().parents[1]` finds the project root folder (one level above `src/`), so the CSV path is always correct no matter which folder you run the code from.

### 5.2 The player skill profiles

```python
PLAYER_PROFILES = {
    "Tamim Iqbal": (38, 82),
    "Shakib Al Hasan": (36, 88),
    "Mushfiqur Rahim": (37, 84),
    "Litton Das": (34, 95),
    ...
}
```

Each player gets two numbers: **mean runs per innings** (roughly how many runs he usually scores) and **strike-rate tendency** (roughly how fast he scores). Tamim Iqbal (38, 82) usually scores around 38 runs at a strike rate around 82. Litton Das (34, 95) has a lower mean but a higher strike-rate tendency — he scores faster but gets out for fewer runs on average. These profiles make the seven players **different from each other**, like real life. The file also lists 8 `OPPONENTS` and 3 `VENUES` (`Home`, `Away`, `Neutral`).

### 5.3 The random seed — why 42?

```python
rng = np.random.default_rng(42)
n = 360
```

`rng` is the **random number generator**, and **42** is the **seed** — the starting point of the random sequence. With the same seed, the "random" numbers come out **exactly the same every run**. This matters in data science: anyone who runs the code gets the same dataset and the same results, so the work can be checked and reproduced. `n = 360` is the number of innings to create.

### 5.4 Picking players, opponents and venues

```python
player = rng.choice(players, size=n)
opponent = rng.choice(OPPONENTS, size=n)
venue = rng.choice(VENUES, size=n, p=[0.45, 0.35, 0.20])
```

`rng.choice(...)` picks random items from a list, 360 times. For venue, `p=[0.45, 0.35, 0.20]` sets the probabilities: 45% Home, 35% Away, 20% Neutral (they add up to 1). The code then looks up each chosen player's two profile numbers into arrays called `mean_runs` and `sr_tendency`, so every row knows "my player's usual runs" and "my player's usual strike rate".

### 5.5 Generating runs

```python
runs = np.clip(rng.normal(mean_runs, 22), 0, 160).round().astype(int)
```

`rng.normal(mean_runs, 22)` draws runs from a **normal distribution** (bell curve) centred on the player's mean, with spread (standard deviation) 22 — so Tamim's innings are usually near 38 but can be much lower or higher, like real cricket. `np.clip(..., 0, 160)` keeps values sensible: no negative runs, nothing above 160. `.round().astype(int)` makes them whole numbers.

### 5.6 Deriving balls faced

Balls are **not** drawn directly. They are calculated from runs and the player's strike-rate tendency, so the data stays realistic:

```python
effective_sr = np.clip(rng.normal(sr_tendency, 12), 40, 180)
balls_faced = np.where(
    runs > 0,
    np.maximum(1, np.round(runs / (effective_sr / 100) + rng.normal(0, 3, size=n))),
    rng.integers(1, 9, size=n),
)
```

`effective_sr` is this innings' strike rate: the player's tendency plus randomness (spread 12, clipped to 40–180). If the player scored runs, balls ≈ runs ÷ (strike rate / 100), plus a little noise, and at least 1 ball. If the player scored 0 (a "duck"), he still faced 1 to 8 balls.

### 5.7 Deriving fours and sixes

```python
boundary_share = rng.uniform(0.30, 0.65, size=n) * runs
sixes = (boundary_share * rng.uniform(0.2, 0.5, size=n) // 6).astype(int)
fours = ((boundary_share - sixes * 6) // 4).astype(int)
```

Between 30% and 65% of the runs are assumed to come from boundaries. Part of that boundary share becomes sixes (6 runs each) and the rest becomes fours (4 runs each). One safety fix follows in the code: if 4×fours + 6×sixes is somehow more than the total runs, some fours are removed — boundary runs can never exceed total runs, and the code enforces that.

### 5.8 Dismissal, strike rate and match result

```python
dismissal = np.where(rng.random(n) < 0.15, "Not Out", "Out")
strike_rate = np.round(runs / balls_faced * 100, 2)
match_result = rng.choice(["Won", "Lost"], size=n, p=[0.5, 0.5])
```

Each innings has a **15% chance** of being `Not Out`, otherwise `Out`. `strike_rate` uses the exact cricket formula (runs ÷ balls × 100). `match_result` is a fair coin toss: 50% Won, 50% Lost.

### 5.9 Building the table and saving the CSV

```python
df = pd.DataFrame({ "match_id": ..., "player": player, ... })
DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(DATA_PATH, index=False)
```

All columns are packed into a Pandas **DataFrame** (a table), with `match_id` values `M-001` … `M-360`. `mkdir(...)` creates the `data/` folder if it does not exist, and `to_csv(..., index=False)` saves the CSV without writing Pandas' row numbers as an extra column.

---

## 6. Code explanation: `src/analysis.py`

This file **analyses** the data: it reads the CSV and produces every table, chart and the insights file.

### 6.1 Setup and chart style

Imports and paths work the same way as in the generator. The chart style is set with a fallback:

```python
try:
    plt.style.use("seaborn-v0_8-whitegrid")
except OSError:
    plt.style.use("ggplot")
```

It tries a clean Seaborn-style grid theme; if that style is missing in your Matplotlib version, it uses `ggplot` instead of crashing. There is also a helper function `save_bar_chart(...)`: it receives a Pandas Series, a title and labels, draws a blue bar chart, tilts the x-axis labels so long names fit, and saves the PNG at 160 dpi. Charts 1 and 4 use this helper, so their code stays short.

### 6.2 Loading and cleaning the data

```python
df = pd.read_csv(DATA_PATH)
df = df.drop_duplicates().copy()
numeric_cols = ["runs", "balls_faced", "fours", "sixes", "strike_rate"]
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors="coerce")
df = df.dropna(subset=numeric_cols)
```

`read_csv` loads the whole CSV into a DataFrame called `df`. `drop_duplicates()` removes repeated rows. `pd.to_numeric(..., errors="coerce")` forces the number columns to be real numbers — anything that is not a number becomes `NaN` (missing) instead of crashing. `dropna(...)` then removes rows where those key numbers are missing. Clean data in, trustworthy results out.

### 6.3 Helper columns

```python
df["times_out"] = np.where(df["dismissal"] == "Out", 1, 0)
df["is_fifty"] = np.where((df["runs"] >= 50) & (df["runs"] < 100), 1, 0)
df["is_hundred"] = np.where(df["runs"] >= 100, 1, 0)
```

Three new 0/1 columns make counting easy: `times_out` is 1 when the player got out (adding it up gives total dismissals — needed for the batting average), `is_fifty` is 1 for scores of 50–99, and `is_hundred` is 1 for scores of 100+. Adding up a 0/1 column is a common Pandas trick for counting.

### 6.4 The overall summary table

```python
df.describe(include="all").round(2).to_csv(TABLE_DIR / "summary_statistics.csv")
```

`describe()` gives count, mean, standard deviation, minimum, maximum and quartiles for every column in one go.

### 6.5 The player summary — the heart of the analysis

```python
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
player_summary["batting_average"] = player_summary["total_runs"] / player_summary["times_out"]
```

`groupby("player")` splits the 360 rows into 7 groups, one per player. `.agg(...)` calculates several summaries per group at once: innings, total runs, times out, mean strike rate, number of 50s, number of 100s and highest score. Then the **batting average** is calculated the proper cricket way: **total runs ÷ times out** (not total runs ÷ innings). The table is rounded to 2 decimals, sorted by batting average (best first) and saved as `player_summary.csv`.

### 6.6 Opponent table and correlation table

The opponent table uses the same groupby idea, grouped by `opponent`, with innings, total runs, `avg_runs` (mean) and mean strike rate, sorted so the easiest opponent to score against is on top. The correlation table is one line:

```python
corr = df[["runs", "balls_faced", "fours", "sixes", "strike_rate"]].corr(numeric_only=True).round(2)
```

`.corr()` builds the **correlation matrix**: every pair of number columns gets a value from −1 to +1. Near +1 means "when one goes up, the other goes up too"; near 0 means no clear relationship.

### 6.7 The four charts

- **Chart 1 — Batting Average by Player** (bar chart, uses the helper): it passes `player_summary.set_index("player")["batting_average"]` to `save_bar_chart(...)`. Bars make it easy to compare players side by side.
- **Chart 2 — Strike Rate vs Runs** (scatter plot): `ax.scatter(df["runs"], df["strike_rate"], alpha=0.65, ...)`. Each dot is one innings — x = runs, y = strike rate. `alpha=0.65` makes dots slightly transparent so overlapping dots stay visible.
- **Chart 3 — Distribution of Runs per Innings** (histogram): `ax.hist(df["runs"], bins=18, ...)` groups innings into 18 ranges ("bins") and counts how many fall in each; `ax.axvline(df["runs"].mean(), ...)` draws a dashed line at the mean score.
- **Chart 4 — Average Runs by Opponent** (bar chart, uses the helper): the `avg_runs` column of the opponent table drawn as bars.

Every chart ends with `fig.savefig(..., dpi=160)` to save a clear PNG, and `plt.close(fig)` to free memory.

### 6.8 Writing insights.md automatically

At the end, the code picks the key rows from the tables. `player_summary.iloc[0]` is the first row after sorting — the highest batting average. For strike rate, it first filters to players with **30 or more innings** (a variable called `regulars`), so a player with 2 lucky innings cannot "win" unfairly, then takes the maximum `avg_strike_rate`. `idxmax()` finds the rows with the most hundreds and the most total runs. These values are placed into a Markdown text (an f-string) and saved with `INSIGHTS_PATH.write_text(...)` — so `outputs/insights.md` is written by the program, not by hand. Finally the code prints a short summary to the terminal.

---

## 7. How to read the outputs

**Charts**

- **average_runs_by_player.png** — Compare bar heights: the tallest bar is the most consistent run-scorer by the official average definition. Remember, this average uses times out, so not-out innings help a player.
- **strike_rate_vs_runs.png** — Look at the shape of the dot cloud. Dots trend up and to the right: bigger innings usually come with higher strike rates. Single dots far from the cloud are unusual innings (for example, many runs at a very low strike rate).
- **runs_distribution.png** — Most innings are small scores (tall bars on the left) and big scores are rare (bars shrink to the right). This "long tail" shape is typical of real batting data too. The dashed line is the mean.
- **average_runs_by_opponent.png** — The tallest bar is the opponent against whom batters scored most freely in this data.

**Tables**

- **player_summary.csv** — The main result table. It answers almost every project question: averages, strike rates, 50s, 100s, highest scores.
- **performance_by_opponent.csv** — Check `avg_runs` to see which opponent was easiest or hardest to score against.
- **correlation_matrix.csv** — Look for pairs near +1. Runs and balls faced are strongly related (more balls → more runs), and runs also move together with fours and sixes. Correlation shows a relationship, **not** a cause.
- **summary_statistics.csv** — A health check of the whole dataset: row count, typical values (mean), spread (std), and the minimum and maximum of every column.

---

## 8. Key results of this project

These are the actual results from `outputs/insights.md` (synthetic practice data — not real statistics):

- Dataset size: **360 innings** across **7 players**.
- Highest batting average: **Mushfiqur Rahim — 46.88**.
- Highest average strike rate (players with 30+ innings): **Towhid Hridoy — 100.00**.
- Most centuries: **Tamim Iqbal — 1 century**.
- Most total runs: **Litton Das — 2,281 runs in 69 innings**.
- Best opponent to bat against (highest average runs): **Pakistan — 40.10 average runs per innings**.

---

## 9. Viva / presentation help

Questions a teacher may ask, with short model answers.

**Q1. What is the difference between batting average and mean runs?**
Mean runs = total runs ÷ total innings. Batting average = total runs ÷ times out. Not-out innings are excluded from the denominator in batting average, so it is usually higher — and it is the official cricket measure.

**Q2. How is strike rate calculated, and why can it mislead?**
Strike rate = runs ÷ balls faced × 100. It can mislead because a player who scores 20 runs from 10 balls and gets out has a strike rate of 200, yet he did not help the team much. Always read strike rate together with runs and average.

**Q3. Why did you use Pandas `groupby`?**
Because the questions are per-group questions: per player and per opponent. `groupby` splits the table into groups and `agg` calculates count, sum, mean and max for each group in a few lines — much safer than writing loops by hand.

**Q4. Why is the random seed fixed at 42?**
For reproducibility. Anyone who runs the generator gets exactly the same dataset, charts and findings. Without a seed, the numbers would change on every run and nobody could verify the work.

**Q5. Balls faced were generated from runs — how?**
Balls ≈ runs ÷ (strike rate / 100), using each player's strike-rate tendency plus a little random noise. This keeps runs, balls and strike rate consistent with each other, like real scorecards.

**Q6. Is this real data? What is synthetic data?**
No. Synthetic data is artificial data created by a program to imitate the shape of real data. The player names are real, but every number was generated with NumPy for practice, so the findings must never be quoted as real career statistics.

**Q7. What does the correlation matrix tell you?**
It shows how strongly two number columns move together, from −1 to +1. Runs and balls faced are strongly positively correlated. But correlation is not causation — facing more balls does not force runs; good innings simply last longer.

**Q8. Why filter to players with 30+ innings for the best strike rate?**
To avoid a small-sample fluke. A player with only 2 innings could top the list by luck. A minimum-innings rule makes the comparison fair — the same rule real cricket records use.

**Q9. What does the histogram of runs show?**
Most innings end with low scores and only a few innings are big. The distribution is right-skewed (a long tail to the right), which is why the mean is higher than the most common scores.

**Q10. How would you do this project with real data?**
Collect real scorecards (for example from ESPNcricinfo), save them in the same CSV format with the same columns, and run the same `analysis.py`. The analysis code would not need to change — only the data source changes.

---

## 10. What to learn next / how to extend

1. **Use real data** — download real Bangladesh match scorecards from ESPNcricinfo or Kaggle, convert them to the same 11-column format, and compare the real findings with these practice ones.
2. **Add bowling analysis** — wickets, economy rate and bowling average, using the same groupby pattern.
3. **Try Machine Learning** — use scikit-learn to predict a player's runs from balls faced, opponent and venue, and check how accurate the prediction is.
4. **Build a dashboard** — turn the charts into an interactive Streamlit app where a user can pick a player and see only his statistics.

---

*End of guide. If you can explain Sections 3, 5, 6 and 9 in your own words, you fully understand this project.*
