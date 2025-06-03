#!/usr/bin/python3

"""
Module that defines a class Student
"""

class Student:
    """Class that defines a student"""
    def __init__(self, first_name, last_name, age):
        """Initializes the student with first name, last name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns the dictionary description with simple data structure
        (list, dictionary, string, integer and boolean) for JSON serialization of the object

        args:
            self: Object to be serialized
        """
        return self.__dict__
