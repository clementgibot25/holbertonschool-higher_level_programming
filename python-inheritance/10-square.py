#!/usr/bin/python3

'''
This module defines a class Square that inherits from Rectangle.
'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''
    A class that inherits from Rectangle.
    '''

    def __init__(self, size):
        '''
        Initialize a new Square instance.

        Args:
            size (int): The size of the square.

        Raises:
            ValueError: If size is less than or equal to 0.
        '''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
