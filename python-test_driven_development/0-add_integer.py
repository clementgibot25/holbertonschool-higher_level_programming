#!/usr/bin/python3
"""
add_integer module
"""
def add_integer(a, b=98):
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
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
