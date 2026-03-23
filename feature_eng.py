import pandas as pd
from rich.console import Console
import numpy as np

console = Console()

df = pd.read_csv(r"C:\Users\DELL\Downloads\netflix.csv")
console.print("[bold magenta]Feature Engineering[/bold magenta]")

console.print("\n[bold yellow]Creating 'release_age' Feature:[/bold yellow]")
df['release_age'] = 2026 - df['release_year']
console.print(df[['release_year', 'release_age']].head())

console.print("\n[bold green]Creating 'is_recent' Feature:[/bold green]")
df['is_recent'] = df['release_year'] >= 2018
console.print(df[['release_year', 'is_recent']].head())

console.print("\n[bold cyan]Creating 'seasons' Feature:[/bold cyan]")
df['seasons'] = df['duration'].apply(
    lambda x: int(x.split(' ')[0]) if isinstance(x, str) and 'Season' in x else 0
)
console.print(df[['duration', 'seasons']].head())

console.print("\n[bold red]Creating 'content_length_category' Feature:[/bold red]")
df['duration_mins'] = pd.to_numeric(df['duration'].str.extract(r'(\d+)')[0], errors='coerce')

conditions = [
    df['duration_mins'] < 60,
    (df['duration_mins'] >= 60) & (df['duration_mins'] < 120),
    df['duration_mins'] >= 120
]
choices = ['Short', 'Medium', 'Long']

df['content_length_category'] = np.select(conditions, choices, default='Unknown')
console.print(df[['duration_mins', 'content_length_category']].head())