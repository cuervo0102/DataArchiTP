import pandas as pd
from rich.console import Console
import numpy as np

from exploration_data import show_counts


console = Console()
df = pd.read_csv(r"C:\Users\DELL\Downloads\netflix.csv")
console.print("[bold magenta]Analyse Métier[/bold magenta]")


num_movies = (df['type'] == 'Movie').sum()
console.print("Nombre total de films (Movies):", num_movies)

num_tv_shows = (df['type'] == 'TV Show').sum()
console.print("Nombre total de séries (TV Shows):", num_tv_shows)

console.print("\n[bold yellow]Top 5 des pays avec le plus de films :[/bold yellow]")
show_counts("Top 5 des pays", df['country'].value_counts().head(5))


console.print("\n[bold green]Nombre contenus par année de sortie :[/bold green]")
show_counts("Contenus par année de sortie", df['release_year'].value_counts().sort_index())


console.print("\n[bold cyan]Nombre moyenne des film :[/bold cyan]")
average_duration = pd.to_numeric(df['duration'].str.extract(r'(\d+)')[0], errors='coerce').mean()
console.print(f"Durée moyenne des films : {average_duration:.2f} minutes")


