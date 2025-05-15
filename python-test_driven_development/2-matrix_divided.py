#!/usr/bin/python3

"""
matrix_divided module
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.
    Args:
        matrix (list of lists): The matrix to be divided.
        div (int or float): The number to divide the matrix elements by.
    Returns:
        list of lists: A new matrix with all elements divided by div.
    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If div is not an integer or float.
        ZeroDivisionError: If div is zero.
    """
    if not isinstance(matrix, list) or not all(
        isinstance(row, list) and all(
            isinstance(x, (int, float)) for x in row
        ) for row in matrix
    ):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if len(matrix) > 0:
        size = len(matrix[0])
        if not all(len(row) == size for row in matrix):
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(x / div, 2) for x in row] for row in matrix]
