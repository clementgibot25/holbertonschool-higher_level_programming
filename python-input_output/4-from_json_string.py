#!/usr/bin/python3

"""
Module that returns an object (Python data structure) represented
by a JSON string
"""


import json


def from_json_string(my_str):
    """returns an object (Python data structure) represented by a JSON string

    args:
        my_str: JSON string to be deserialized
    """
    return json.loads(my_str)
