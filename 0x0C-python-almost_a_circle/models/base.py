#!/usr/bin/python3
"""Module contains the base class"""


import json


class Base:
    """The base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initilizes object id

        Arg:
            id(int): the id to assign
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """changes dictionaries to JSON strings"""
        if list_dictionaries is None or 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves a list of instances"""
        filename = cls.__name__ + ".json"
        jlist = []
        if list_objs is not None:
            for item in list_objs:
                jlist.append(cls.to_dictionary(item))
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(jlist))

    @staticmethod
    def from_json_string(json_string):
        """creates a list from a JSON string"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """creates a new shape from a dictionary"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """This method creates a new shape from a file"""
        filename = cls.__name__ + ".json"
        result = []
        try:
            with open(filename, mode="r") as fin:
                result = cls.from_json_string(fin.read())
            for i in range(len(result)):
                result[i] = cls.create(**result[i])
        except:
            result = []
        return result
