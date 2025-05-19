#!/usr/bin/python3
"""
Module for Square class with private size attribute.
"""


class Square:
    """
    Defines a square with a private size attribute.
    
    Attributes:
        __size (int): The size of the square (private).
    """
    def __init__(self, size):
        """
        Initialize a Square instance with a given size.
        
        Args:
            size (int): The size of the square.
        """
        self.__size = size
