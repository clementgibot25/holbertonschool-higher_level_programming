#!/usr/bin/python3
"""
add_integer module
"""
def add_integer(a, b):
    """
    Adds two integers and returns the result.
    
    Args:
        a (int): The first integer.
        b (int): The second integer.
    
    Returns:
        int: The sum of the two integers.
    
    Raises:
        TypeError: If either `a` or `b` is not an integer.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")
    return int(a) + int(b)
