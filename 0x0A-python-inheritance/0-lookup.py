#!/usr/bin/python3
"""Module gets object properties"""


def lookup(obj):
    """Function returns the list of available attributes and
    methods of an object

    Arg:
        obj(object): the object to be searched
    """
    return dir(obj)
