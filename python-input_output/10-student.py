#!/usr/bin/python3

"""
Module that defines a class Student with JSON serialization
"""


class Student:
    """Class that defines a student"""
    def __init__(self, first_name, last_name, age):
        """Initializes the student with first name, last name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance
        If attrs is a list of strings, only attributes contained in this list
        are retrieved. Otherwise, all attributes are retrieved.

        Args:
            attrs (list, optional): List of attribute names to include.
                                 If None, all attributes are included.

        Returns:
            dict: Dictionary representation of the Student instance
        """
        if isinstance(attrs, list) and \
           all(isinstance(attr, str) for attr in attrs):
            return {
                key: getattr(self, key)
                for key in attrs if hasattr(self, key)
            }
        return self.__dict__
