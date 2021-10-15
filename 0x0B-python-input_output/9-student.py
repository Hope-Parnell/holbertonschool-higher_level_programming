#!/usr/bin/python3
"""Module contains the Student class"""


class Student:
    """Class for students"""
    def __init__(self, first_name, last_name, age):
        """initializes a student

        Args:
            first_name(str): the student's first name
            last_name(str): the student's last name
            age(int): the student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns the dictionary for a student"""
        return self.__dict__
