#!/usr/bin/python3
"""This Module prints a name"""


def say_my_name(first_name, last_name=""):
    """Function to print a person's name

    Args:
        first_name(string): the person's first name
        last_name(string): the person's last name, defaults to empty
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
