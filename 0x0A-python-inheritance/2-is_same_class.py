#!/usr/bin/python3
"""Module checks the class of an object"""


def is_same_class(obj, a_class):
    """Function checks if the object is exactly an
    instance of the specified class

    Args:
        obj(object): the object to check
        a_class(class): the class to check against
    """
    return True if type(obj) is a_class else False
