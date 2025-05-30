#!/usr/bin/python3

'''
This module defines a class BaseGeometry with a method area.
'''


class BaseGeometry:
    '''
    A class with a method area that raises an exception.
    '''

    def area(self):
        '''
        Raises an exception indicating that the area method is not implemented.
        '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''
        Validate that a value is an integer greater than 0.
        '''
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
