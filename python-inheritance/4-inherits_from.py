#!/usr/bin/python3
"""
This module contains a function that checks if an object is an instance
of a class that inherited (directly or indirectly) from the specified class.
"""


def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    Args:
        obj: The object to check
        a_class: The class to check against

    Returns:
        bool: True if obj is an instance of a class
        that inherited from a_class,
        False otherwise or if obj is an instance of a_class itself
    """
    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
