#!/usr/bin/python3
"""
This module provides a function to list all available attributes
and methods of an object.
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        list: A list containing the names of attributes and methods.
    """
    return dir(obj)
