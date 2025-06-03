#!/usr/bin/python3

"""
Module that creates an Object fom a "JSON" file
"""

import json


def load_from_json_file(filename):
    """creates an Object fom a "JSON" file

    args:
        filename: Name of the file to create an object from
    """
    with open(filename, "r", encoding="utf-8") as newfile:
        return json.load(newfile)
