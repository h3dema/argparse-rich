import argparse
from rich.console import Console
from rich.markdown import Markdown
from rich.style import Style


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Markdown viewer")
    parser.add_argument("fname", type=str, help="Name of the markdown file")
    args = parser.parse_args()

    console = Console()
    with open(args.fname) as f:
        MARKDOWN = f.read()
    md = Markdown(MARKDOWN)
    console.clear(home=True)
    console.print("Contents of {}:".format(args.fname), style=Style(bold=True, reverse=True), justify="center")
    console.print(md)
