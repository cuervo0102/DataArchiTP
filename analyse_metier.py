import pandas as pd
import numpy as np
from rich.console import Console

from exploration_data import show_counts

console = Console()


def analyse(df: pd.DataFrame) -> None:
    """Run business analysis on the provided DataFrame (read-only)."""
    console.print("[bold magenta]Analyse Métier[/bold magenta]")

    num_movies = (df["type"] == "Movie").sum()
    console.print(f"Nombre total de films (Movies) : {num_movies}")

    num_tv_shows = (df["type"] == "TV Show").sum()
    console.print(f"Nombre total de séries (TV Shows) : {num_tv_shows}")

    console.print("\n[bold yellow]Top 5 des pays avec le plus de contenus :[/bold yellow]")
    show_counts("Top 5 des pays", df["country"].value_counts().head(5))

    console.print("\n[bold green]Nombre de contenus par année de sortie :[/bold green]")
    show_counts("Contenus par année de sortie", df["release_year"].value_counts().sort_index())

    console.print("\n[bold cyan]Durée moyenne des films :[/bold cyan]")
    movies_only = df[df["type"] == "Movie"].copy()
    average_duration = pd.to_numeric(
        movies_only["duration"].str.extract(r"(\d+)")[0], errors="coerce"
    ).mean()
    console.print(f"Durée moyenne des films : {average_duration:.2f} minutes")


if __name__ == "__main__":
    df = pd.read_csv(r"C:\Users\DELL\Downloads\netflix_engineered.csv")
    analyse(df)