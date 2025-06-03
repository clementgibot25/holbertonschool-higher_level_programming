#!/usr/bin/python3

"""
Module appends a string to a text file(UTF8) and returns
the number of characters appended
"""


def append_write(filename="", text=""):
    """appends a string to a text file(UTF8) and returns
        the number of characters appended

    args:
        filename: Name of the file appended to
        text: String to be appended to the file
    """
    with open(filename, "a", encoding="utf-8") as newfile:
        return newfile.write(text)
