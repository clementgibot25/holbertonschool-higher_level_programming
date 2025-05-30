#!/usr/bin/python3

'''
This module defines a class Rectangle that inherits from BaseGeometry.
'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


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

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
        '''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        '''
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle (width * height).
        '''
        return self.__width * self.__height

    def __str__(self):
        '''
        Return a string representation of the rectangle.

        Returns:
            str: The string representation of the rectangle.
        '''
        return f"[Rectangle] {self.__width}/{self.__height}"
