#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        if not row:
            print()
            continue
        for i, num in enumerate(row):
            end = " " if i < len(row) - 1 else ""
            print("{:d}".format(num), end=end)
        print()
