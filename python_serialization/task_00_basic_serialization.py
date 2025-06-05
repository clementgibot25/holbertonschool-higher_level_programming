#!/usr/bin/python3

import json

def serialize_and_save_to_file(data, filename):
    """Serialize a Python dictionary to a JSON file.

    Args:
        data (dict): A Python dictionary with data to serialize.
        filename (str): The name of the file where the JSON data will be saved.
    """
    with open(filename, 'w') as file:
        json.dump(data, file)

def load_and_deserialize(filename):
    """Load and deserialize a JSON file to a Python dictionary.

    Args:
        filename (str): The name of the JSON file to load.

    Returns:
        dict: A Python dictionary with the deserialized JSON data.
    """
    with open(filename, 'r') as file:
        return json.load(file)
