#!/usr/bin/python3
"""
Module for text_indentation function.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The text to process

    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    seps = ".?:"
    line = ""
    for c in text:
        line += c
        if c in seps:
            print(line.strip())
            print()
            line = ""
            continue
    if line.strip():
        print(line.strip())

