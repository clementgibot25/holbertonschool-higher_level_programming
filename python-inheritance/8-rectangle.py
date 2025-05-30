#!/usr/bin/python3

'''
This module defines a class Rectangle that inherits from BaseGeometry.
'''


class Rectangle(BaseGeometry):
    '''
    A class that inherits from BaseGeometry.
    '''

    def __init__(self, width, height):
        '''
        Initialize a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        '''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
