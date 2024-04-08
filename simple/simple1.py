import argparse

"""
This program does not do any useful action, but it shows the two basic lines for creating the input arguments, i.e., the creation of a parser that reads the possible arguments.
"""

if __name__ == "__main__":

    parser = argparse.ArgumentParser()  # create a parser
    parser.parse_args()  # retrieve the arguments from the command line
