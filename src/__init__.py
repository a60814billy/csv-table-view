from argparse import ArgumentParser
from csv import DictReader
from pathlib import Path

from rich.console import Console
from rich.table import Table


def main():
    parser = ArgumentParser()
    parser.add_argument("csv_file_path", type=str, help="Path to the CSV file")

    args = parser.parse_args()

    if not Path(args.csv_file_path).exists():
        print("File does not exist")
        return

    table = Table()
    rows = []
    with open(args.csv_file_path, "r") as file:
        csv_reader = DictReader(file)
        for c in csv_reader.fieldnames:
            table.add_column(c)
        for row in csv_reader:
            table.add_row(*[row[c] for c in csv_reader.fieldnames])

    console = Console()
    console.print(table, style="grey78")


if __name__ == "__main__":
    main()
