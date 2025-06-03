#!/usr/bin/python3

"""
Module writes a string to a text file(UTF8) and returns the number of characters written
"""


def write_file(filename="", text=""):
    """writes a string to a text file(UTF8) and returns the number of characters written

    args:
        filename: Name of the file written to
        text: String to be written to the file
    """
    with open(filename, "w", encoding="utf-8") as newfile:
        return newfile.write(text)
