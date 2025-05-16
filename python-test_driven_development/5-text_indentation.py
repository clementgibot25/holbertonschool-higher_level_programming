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

    i = 0
    while i < len(text):
        # Skip spaces at the beginning of a line
        while i < len(text) and text[i] == ' ':
            i += 1
        
        # Print current character if we haven't reached the end
        if i < len(text):
            print(text[i], end="")

        # If character is special, print two newlines and skip following spaces
        if i < len(text) and text[i] in '.?:':
            print("\n\n", end="")
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        
        i += 1
