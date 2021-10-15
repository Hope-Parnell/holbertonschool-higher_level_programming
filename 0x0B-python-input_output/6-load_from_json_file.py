#!/usr/bin/python3
"""Module loads a JSON file and creates an object"""


import json


def load_from_json_file(filename):
    """Creates an object from a JSON file

    Arg:
        filename(str): the file to load from
    """
    with open(filename) as f:
        return json.loads(f.read())
