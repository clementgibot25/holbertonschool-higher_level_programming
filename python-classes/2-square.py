#!/usr/bin/python3
"""
Module for Square class with size validation.
"""


class Square:
    """
    Defines a square with a private size attribute and validation.

    Attributes:
        __size (int): The size of the square (private).
    """
    def __init__(self, size=0):
        """
        Initialize a Square instance with a given size.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
