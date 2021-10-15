#!/usr/bin/python3
"""Module opens and reads from a file"""


def read_file(filename=""):
    """Prints file content to standard output

    Arg:
        filename(str): the file to print
    """
    with open(filename) as f:
        print(f.read(), end = "")
