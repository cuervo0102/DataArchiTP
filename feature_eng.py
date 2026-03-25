import pandas as pd
import numpy as np
from rich.console import Console

console = Console()


def engineer(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add engineered features to the DataFrame and return it.
    Operates on a copy to avoid mutating the caller's object.
    """
    df = df.copy()
    console.print("[bold magenta]Feature Engineering[/bold magenta]")

    console.print("\n[bold yellow]Creating 'release_age' feature:[/bold yellow]")
    df["release_age"] = 2026 - df["release_year"]
    console.print(df[["release_year", "release_age"]].head())

    console.print("\n[bold green]Creating 'is_recent' feature:[/bold green]")
    df["is_recent"] = df["release_year"] >= 2018
    console.print(df[["release_year", "is_recent"]].head())

    console.print("\n[bold cyan]Creating 'seasons' feature:[/bold cyan]")
    df["seasons"] = df["duration"].apply(
        lambda x: int(x.split(" ")[0]) if isinstance(x, str) and "Season" in x else 0
    )
    console.print(df[["duration", "seasons"]].head())

    console.print("\n[bold red]Creating 'content_length_category' feature:[/bold red]")
    df["duration_mins"] = pd.to_numeric(
        df["duration"].str.extract(r"(\d+)")[0], errors="coerce"
    )
    conditions = [
        df["duration_mins"] < 60,
        (df["duration_mins"] >= 60) & (df["duration_mins"] < 120),
        df["duration_mins"] >= 120,
    ]
    df["content_length_category"] = np.select(
        conditions, ["Short", "Medium", "Long"], default="Unknown"
    )
    console.print(df[["duration_mins", "content_length_category"]].head())

    return df  


if __name__ == "__main__":
    raw = pd.read_csv(r"C:\Users\DELL\Downloads\netflix_clean.csv")
    engineered = engineer(raw)
    engineered.to_csv(r"C:\Users\DELL\Downloads\netflix_engineered.csv", index=False)
    console.print("[bold green]Saved → netflix_engineered.csv[/bold green]")