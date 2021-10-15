#!/usr/bin/python3
"""Module saves an object to a file as a JSON string"""


import json


def save_to_json_file(my_obj, filename):
    """Saves an object as a JSON in a file

    Args:
        my_obj(obj): object to encode and save
        filename(str): name of the file to write to
    """
    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))
