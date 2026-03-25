import pandas as pd
from rich.console import Console
from rich.table import Table

console = Console()


def clean(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the DataFrame:
      - Report missing values before and after.
      - Drop rows with any null values.
      - Return the cleaned copy.
    """
    console.print("[bold magenta]Data Cleaning[/bold magenta]")

    console.print("\n[bold yellow]Missing Values Before Cleaning:[/bold yellow]")
    console.print(df.isnull().sum())

    missing_percentage = (df.isnull().sum() / len(df)) * 100
    console.print("\n[bold cyan]Missing Values Percentage:[/bold cyan]")
    table = Table(title="Missing Values Percentage")
    table.add_column("Column", style="cyan")
    table.add_column("Missing %", style="magenta")
    for column, percentage in missing_percentage.items():
        table.add_row(column, f"{percentage:.2f}%")
    console.print(table)

    df = df.dropna().reset_index(drop=True)

    console.print("\n[bold green]Missing Values After Cleaning:[/bold green]")
    console.print(df.isnull().sum())
    console.print(f"[bold green]Rows remaining: {len(df)}[/bold green]")

    return df  


if __name__ == "__main__":
    raw = pd.read_csv(r"C:\Users\DELL\Downloads\netflix.csv")
    cleaned = clean(raw)
    cleaned.to_csv(r"C:\Users\DELL\Downloads\netflix_clean.csv", index=False)
    console.print("[bold green]Saved → netflix_clean.csv[/bold green]")