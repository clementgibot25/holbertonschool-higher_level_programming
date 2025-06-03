#!/usr/bin/python3
"""
Module that returns a list of lists of integers representing
the Pascal's triangle of n
"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing Pascal's triangle of n

    Args:
        n (int): Number of rows to generate

    Returns:
        list: List of lists representing Pascal's triangle
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]  # First element is always 1

        # Calculate middle elements
        for j in range(1, i):
            new_row.append(prev_row[j-1] + prev_row[j])

        new_row.append(1)  # Last element is always 1
        triangle.append(new_row)

    return triangle
