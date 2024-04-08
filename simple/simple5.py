import os
import argparse
import logging
from typing import Callable, Any
from rich.logging import RichHandler
from rich import print as rprint


"""
add optional arguments to enrich the output
"""

if __name__ == "__main__":
    DEFAULT_FILENAME: str = os.path.basename(__file__).replace(".py", ".log")
    parser = argparse.ArgumentParser()  # create a parser
    # create a argument that receives a text
    parser.add_argument("-f",
                        dest="fname",
                        type=str,
                        default=DEFAULT_FILENAME,
                        metavar="FILENAME",
                        help=f"Enter the name of the file. default: {DEFAULT_FILENAME}"
                        )

    parser.add_argument("--rich",
                        action="store_true",
                        required=False,  # by default, required is False
                        help="enrich the output (on stdout/log)")

    output: argparse.ArgumentParser = parser.add_mutually_exclusive_group(required=True)
    output.add_argument("--log", dest="output", action="store_const", const="log", help="output to log")
    output.add_argument("--file", dest="output", action="store_const", const="file", help="output to a file `fname`")
    output.add_argument("--stdout", dest="output", action="store_const", const="out", help="output to standard output")
    # output.set_defaults(output="out")  # default to stdout (not needed in a mutually_exclusive_group)

    args: argparse.Namespace = parser.parse_args()  # retrieve the arguments from the command line

    if args.rich:
        logging.basicConfig(level=logging.INFO, handlers=[RichHandler()])
        myprint: Callable[..., Any] = rprint
    else:
        logging.basicConfig(level=logging.INFO)
        myprint: Callable[..., Any] = print

    print("Args:", args)

    if args.output == "log":
        # use logging
        logging.info(f"fname: {args.fname}")
        logging.info(f"output: {args.output}")
        logging.info(f"enrich: {args.rich}")

    elif args.output == "file":
        # print to file
        with open(args.fname, "w") as f:
            print("fname:", args.fname, file=f)
            print("output:", args.output, file=f)
            print("enrich:", args.rich, file=f)

    else:  # args.output == "stdout":
        myprint("fname:", args.fname)
        myprint("output:", args.output)
        myprint("enrich:", args.rich)
