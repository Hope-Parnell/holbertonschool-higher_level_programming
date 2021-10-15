#!/usr/bin/python3
"""Module converts JSON to an object"""


import json


def from_json_string(my_str):
    """Converts a json to an object

    Arg:
        my_obj(obj): object to be converted
    """
    return json.loads(my_str)
