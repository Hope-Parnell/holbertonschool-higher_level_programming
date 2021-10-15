#!/usr/bin/python3
"""Module adds a string into a file"""


def append_after(filename="", search_string="", new_string=""):
    """places a new string after a line containing a specific string

    Args:
        filename(str): file to search through
        search_string(str): string to search for
        new_string(str): string to insert
    """
    with open(filename) as f:
        content = ""
        for line in f:
            content += line
            if search_string in line:
                content += new_string
    with open(filename, "w") as f:
        f.write(content)
