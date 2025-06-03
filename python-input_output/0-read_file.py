#!/usr/bin/python3

"""
Module reads file and prints it to stdout
"""


def read_file(filename=""):
    """reads a text file(UTF8) and prints it to stdout

    args:
        filename: Name of the file read
    """
    with open(filename, "r", encoding="utf-8") as newfile:
        print(newfile.read(), end="")
