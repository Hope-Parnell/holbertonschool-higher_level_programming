#!/usr/bin/python3
"""Module checks object subclasses"""


def inherits_from(obj, a_class):
    """Function checks if the object is an instance
    of a class that inherited (directly or indirectly)
    from the specified class

    Args:
        obj(object): the object to check
        a_class: the subclass to check for
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
