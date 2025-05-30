#!/usr/bin/python3

'''
This module defines a class Square that inherits from Rectangle.
'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(BaseGeometry):
    '''
    A class that inherits from BaseGeometry.
    '''

    def __init__(self, size):
        '''
        Initialize a new Square instance.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        '''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
