#!/usr/bin/python3
"""
This module defines a class BaseGeometry with a method area.
"""


class BaseGeometry:
    """
    A class with a method area that raises an exception.
    """

    def area(self):
        """
        Raises an exception indicating that the area method is not implemented.
        """
        raise Exception("area() is not implemented")
