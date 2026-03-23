import pandas as pd
from rich.console import Console
from rich.table import Table

console = Console()

df = pd.read_csv(r"C:\Users\DELL\Downloads\netflix.csv")
console.print("[bold magenta]Data Cleaning[/bold magenta]")

console.print("\n[bold yellow]Missing Values Before Cleaning:[/bold yellow]")
console.print(df.isnull().sum())


missing_percentage = (df.isnull().sum() / len(df)) * 100
console.print("\n[bold cyan]Missing Values Percentage:[/bold cyan]")
missing_table = Table(title="Missing Values Percentage")
missing_table.add_column("Column", style="cyan")
missing_table.add_column("Missing Percentage", style="magenta") 
for column, percentage in missing_percentage.items():
    missing_table.add_row(column, f"{percentage:.2f}%")

console.print(missing_table)

df = df.dropna()
console.print("\n[bold green]Missing Values After Cleaning:[/bold green]")
console.print(df.isnull().sum())


