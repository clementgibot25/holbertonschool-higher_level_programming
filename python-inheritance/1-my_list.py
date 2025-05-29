#!/usr/bin/python3
"""
This module defines a class MyList that inherits from list.
The class includes a method to print the list in ascending sorted order.
"""


class MyList(list):
    """
    A class that inherits from list with additional functionality.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        Assumes all elements of the list are of type int.
        """
        print(sorted(self))
