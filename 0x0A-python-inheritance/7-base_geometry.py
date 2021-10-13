#!/usr/bin/python3
"""Module contains an class with an unimplemented function
and validates values
"""


class BaseGeometry:
    """Class with unimplimented function and a function
    to validate values
    """
    def area(self):
        """Function raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Function validates integers

        Args:
            name(str): name of the variable
            value(object): what is stored in the variable
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value < 0:
            raise ValueError("{} must be greater than 0".format(name))
