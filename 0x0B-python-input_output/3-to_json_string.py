#!/usr/bin/python3
"""Module converts an object to JSON"""


import json


def to_json_string(my_obj):
    """Converts an object to json

    Arg:
        my_obj(obj): object to be converted
    """
    return json.dumps(my_obj)
