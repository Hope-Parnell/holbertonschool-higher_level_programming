#!/usr/bin/python3
"""Module writes to a file"""


def write_file(filename="", text=""):
    """Function writes to a file creating it if it doesn't
    exist or overwriting it if it does

    Args:
        filename(str): the name of the file to be written to
        text(str): content to write to the file
    """
    with open(filename, "w") as f:
        return f.write(text)
