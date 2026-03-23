import pandas as pd
from rich.console import Console
from rich.table import Table

console = Console()

df = pd.read_csv(r"C:\Users\DELL\Downloads\netflix.csv")

console.print("[bold magenta]Data Exploration[/bold magenta]")


console.print("[bold yellow]Columns:[/bold yellow]", df.columns)


console.print("\n[bold green]Head:[/bold green]")
console.print(df.head())


console.print("\n[bold red]Missing Values:[/bold red]")
console.print(df.isnull().sum())



def show_counts(title, series):
    """Helper function to display value counts in a table"""

    
    table = Table(title=title)

    table.add_column("Value", style="cyan")
    table.add_column("Count", style="magenta")

    for index, value in series.items():
        table.add_row(str(index), str(value))

    console.print(table)


show_counts("Type Distribution", df['type'].value_counts())
show_counts("Release Year", df['release_year'].value_counts().head(10))
show_counts("Rating", df['rating'].value_counts())
show_counts("Duration (Top 10)", df['duration'].value_counts().head(10))