
A modular Python pipeline for exploring, cleaning, engineering features from, and analysing the Netflix titles dataset.

---

##  Project Structure

```
.
├── pipeline.py          # Entry point — runs the full pipeline end-to-end
├── exploration_data.py  # Step 2 — exploratory data analysis (read-only)
├── cleaning_data.py     # Step 3 — data cleaning (drops nulls)
├── feature_eng.py       # Step 4 — feature engineering (adds derived columns)
├── analyse_metier.py    # Step 5 — business analysis & metrics
└── README.md
```

---

##  Requirements

- Python 3.8+
- pandas
- numpy
- rich

Install dependencies:

```bash
pip install requirements.txt
```

---

## Dataset

included to this project netflix_csv

 update the `RAW_PATH` constant at the top of `pipeline.py` to match your local path.

---

##  Usage

### Run the full pipeline

```bash
python pipeline.py
or 
python -m pipeline
```

This executes all steps in order and produces two output files:

| File | Description |
|---|---|
| `netflix_clean.csv` | Dataset after null rows are dropped |
| `netflix_engineered.csv` | Dataset with all engineered features added |

### Run a single step independently

Each module can also be executed standalone:

```bash
python exploration_data.py
python cleaning_data.py
python feature_eng.py
python analyse_metier.py
```

> **Note:** Standalone execution reads from the CSV directly. Run them in order so each step has access to the previous step's output.

---

##  Pipeline Steps

### Step 1 — Load
Reads the raw CSV into a pandas DataFrame.

### Step 2 — Explore (`exploration_data.py`)
Read-only analysis of the raw dataset. Outputs:
- Column names and data types
- First 5 rows
- Missing value counts
- Distribution tables: type, release year, rating, duration

### Step 3 — Clean (`cleaning_data.py`)
- Reports missing values and their percentage per column
- Drops all rows containing any null value
- Resets the index
- Saves result to `netflix_clean.csv`

### Step 4 — Feature Engineering (`feature_eng.py`)
Adds the following derived columns:

| Feature | Description |
|---|---|
| `release_age` | `2026 - release_year` |
| `is_recent` | `True` if `release_year >= 2018` |
| `seasons` | Number of seasons (TV Shows only, else `0`) |
| `duration_mins` | Numeric duration in minutes (Movies only) |
| `content_length_category` | `Short` / `Medium` / `Long` based on `duration_mins` |

Saves result to `netflix_engineered.csv`.

### Step 5 — Business Analysis (`analyse_metier.py`)
Read-only metrics on the engineered dataset:
- Total number of Movies vs TV Shows
- Top 5 countries by content count
- Content count per release year
- Average movie duration in minutes

---

##  Architecture

Each module exposes a single public function that accepts a DataFrame and returns a (possibly modified) DataFrame. This makes the pipeline fully composable and testable in isolation.

```
raw CSV
   │
   ▼
explore(df)        # read-only
   │
   ▼
df = clean(df)     # returns cleaned df
   │
   ▼
df = engineer(df)  # returns feature-enriched df
   │
   ▼
analyse(df)        # read-only
```

No module loads the CSV on its own at import time — side effects are gated behind `if __name__ == "__main__"` guards.

---

##  Notes

- `feature_eng.py` operates on a **copy** of the input DataFrame (`df.copy()`) to avoid mutating upstream state.
- Average duration in `analyse_metier.py` is computed on **Movies only**, filtering out TV Shows which have season-based durations.
- All console output is rendered using the [Rich](https://github.com/Textualize/rich) library for readable, colour-coded terminal output.
