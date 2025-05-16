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

    # Initialize variables
    result = ""
    skip_space = False

    # Process each character
    for char in text:
        # If we need to skip spaces and current char is space, continue
        if skip_space and char == " ":
            continue

        # Add the character to result
        result += char

        # If character is special, add two newlines and set skip_space
        if char in ".?:":
            result += "\n\n"
            skip_space = True
        else:
            skip_space = False

    # Print result without trailing spaces
    print(result.strip(), end="")
