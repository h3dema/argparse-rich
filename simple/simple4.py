import argparse

"""
add verbosity (in a list of values and mandatory)
add optional arguments to enrich the output
"""

if __name__ == "__main__":

    parser = argparse.ArgumentParser()  # create a parser
    # create a argument that receives a text
    parser.add_argument("fname",
                        help="enter the name of the file"
                        )
    parser.add_argument("-v", "--verbosity",
                        type=int,  # must be an integer
                        choices=range(4),
                        required=True,  # force the parameter
                        help="increase output verbosity")

    parser.add_argument("--rich",
                        action="store_true",
                        required=False,  # by default, required is False
                        help="enrich the output")

    args = parser.parse_args()  # retrieve the arguments from the command line

    if args.rich:
        # trick: import rich.print overwriting python's default print function
        from rich import print

    print("Args:", args)
    print("fname:", args.fname)
    print("verbosity:", args.verbosity)
    print("enrich:", args.rich)
