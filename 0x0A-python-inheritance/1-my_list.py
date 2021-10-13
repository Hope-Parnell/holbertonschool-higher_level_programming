#!/usr/bin/python3
"""Module creates a class that inherits a list"""


class MyList(list):
    """Class inherits the list built-in"""
    def print_sorted(self):
        """Function prints the sorted list"""
        print(sorted(self))
