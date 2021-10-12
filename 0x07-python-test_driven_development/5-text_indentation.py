#!/usr/bin/python3
"""This module separates a string"""


def text_indentation(text):
    """This function splits a string

    Arg:
        text(string): the string to be split
    """
    separate = False
    split = True
    separators = [".", ":", "?"]
    if type(text) is not str:
        raise TypeError("text must be a string")
    for c in text:
        if separate is True:
            print("\n")
            separate = False
            split = True
        if c is " " and split is True:
            continue
        else:
            if c is not "\n":
                split = False
            print("{}".format(c), end="")
        if c in separators:
            separate = True
