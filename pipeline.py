import pandas as pd
from rich.console import Console

from exploration_data import explore
from cleaning_data import clean
from feature_eng import engineer
from analyse_metier import analyse

RAW_PATH        = r"C:\Users\DELL\Downloads\netflix.csv"
CLEAN_PATH      = r"C:\Users\DELL\Downloads\netflix_clean.csv"
ENGINEERED_PATH = r"C:\Users\DELL\Downloads\netflix_engineered.csv"

console = Console()


def main() -> None:
    console.rule("[bold blue]Step 1 — Load[/bold blue]")
    df = pd.read_csv(RAW_PATH)
    console.print(f"Loaded {len(df):,} rows from {RAW_PATH}")

    console.rule("[bold blue]Step 2 — Explore[/bold blue]")
    explore(df)

    console.rule("[bold blue]Step 3 — Clean[/bold blue]")
    df = clean(df)
    df.to_csv(CLEAN_PATH, index=False)
    console.print(f"[green]Saved → {CLEAN_PATH}[/green]")

    console.rule("[bold blue]Step 4 — Feature Engineering[/bold blue]")
    df = engineer(df)
    df.to_csv(ENGINEERED_PATH, index=False)
    console.print(f"[green]Saved → {ENGINEERED_PATH}[/green]")

    console.rule("[bold blue]Step 5 — Business Analysis[/bold blue]")
    analyse(df)

    console.rule("[bold green]Pipeline complete ✓[/bold green]")


if __name__ == "__main__":
    main()
