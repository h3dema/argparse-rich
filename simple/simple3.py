import argparse

"""
add verbosity (must be an integer)
"""

if __name__ == "__main__":

    parser = argparse.ArgumentParser()  # create a parser
    # create a argument that receives a text
    parser.add_argument("fname",
                        help="enter the name of the file"
                        )
    parser.add_argument("-v", "--verbosity",
                        type=int,  # must be an integer
                        default=1,  #  if nothing is provided, assumes 1
                        # choices=range(0, 40),  # only accepts values from 0 to 39
                        choices=[0, 1, 3, 4],
                        # metavar="{0, 1, ..., 39}",  # change the range shown with -h
                        # metavar="nonsense",  # change the range shown with -h
                        help="increase output verbosity")
    args = parser.parse_args()  # retrieve the arguments from the command line
    print("Args:", args)
    print("fname:", args.fname)
    print("verbosity:", args.verbosity)
