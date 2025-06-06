#!/usr/bin/python3

"""
Module that returns the JSON representation of an object (string)
"""

import json


def to_json_string(my_obj):
    """returns the JSON representation of an object (string)

    args:
        my_obj: Object to be serialized
    """
    return json.dumps(my_obj)
