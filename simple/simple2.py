import argparse

"""
receives a text from the command line
"""

if __name__ == "__main__":

    parser = argparse.ArgumentParser()  # create a parser
    # create a argument that receives a text
    # notice that `help` contains the text that will show with `-h`
    parser.add_argument("fname",
                        help="enter the name of the file"
                        )
    args = parser.parse_args()  # retrieve the arguments from the command line

    print("Args:", args)
    print("fname:", args.fname)
