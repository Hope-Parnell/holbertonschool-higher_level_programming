#!/usr/bin/python3
"""Module checks the class or subclasses of an object"""


def is_kind_of_class(obj, a_class):
    """Function checks if the object is an instance of,
    or if the object is an instance of a class that inherited
    from, the specified class

    Args:
        obj(object): the object to check
        a_class(class): the class to check against
    """
    return True if isinstance(obj, a_class) else False
