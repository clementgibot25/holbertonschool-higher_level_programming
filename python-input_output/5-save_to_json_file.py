#!/usr/bin/python3

"""
Module that writes an object to a text file using JSON representation
"""

import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file using JSON representation

    args:
        my_obj: Object to be serialized
        filename: Name of the file to write to
    """
    with open(filename, "w", encoding="utf-8") as newfile:
        json.dump(my_obj, newfile)
