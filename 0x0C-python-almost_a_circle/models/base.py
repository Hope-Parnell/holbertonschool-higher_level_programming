#!/usr/bin/python3
"""Module contains the base class"""


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
