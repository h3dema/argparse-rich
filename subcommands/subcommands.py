"""

python3 -m pip install rich

"""

import argparse
import logging
from rich import print as rprint


def log_com(log):
    if log.highlight:
        rprint(f"[bold magenta]{log.text}[/bold magenta]")
    else:
        rprint(log.text)


def main():

    parser = argparse.ArgumentParser(description="Example of subcommands")

    parser.add_argument("--debug", action="store_true", help="Set logging to debug")
    subparser = parser.add_subparsers()

    log_p: argparse.ArgumentParser = subparser.add_parser("log")
    log_p.add_argument("text", type=str, nargs="*", default=None)
    log_p.add_argument("--highlight", action="store_true", help="Highlight text")
    log_p.set_defaults(func=log_com)

    show_p: argparse.ArgumentParser = subparser.add_parser("show")
    show_p.add_argument("--all", action="store_true")
    show_p.add_argument("--id", type=int, default=0)
    show_p.add_argument("-s", "--skip", type=int, default=0)
    show_p.add_argument("-l", "--limit", type=int, default=100)

    search_p: argparse.ArgumentParser = subparser.add_parser("search")
    search_p.add_argument("search", type=str, default=None)
    search_p.add_argument("-limit", type=int, default=100)

    args: argparse.Namespace = parser.parse_args()
    logging.basicConfig(level=logging.DEBUG if args.debug else logging.INFO)
    args.func(args)


if __name__ == "__main__":
    main()
