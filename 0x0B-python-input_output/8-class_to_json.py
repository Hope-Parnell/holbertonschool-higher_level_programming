#!/usr/bin/python3
"""Module contains a function that returns the dictionary description
with simple data structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object
"""


def class_to_json(obj):
    """prepares a class for JSON serialization

    Arg:
        obj(class): the class to prepare
    """
    return obj.__dict__
