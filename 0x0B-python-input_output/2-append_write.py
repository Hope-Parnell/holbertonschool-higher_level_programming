#!/usr/bin/python3
"""Module appends text to a file"""


def append_write(filename="", text=""):
    """Function writes to a file appending the
    text if the file already exists

    Args:
        filename(str): the name of the file to be written to
        text(str): content to write to the file
    """
    with open(filename, "a") as f:
        return f.write(text)
