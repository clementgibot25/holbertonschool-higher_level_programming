#!/usr/bin/python3
import json

def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary and saves it to a JSON file.
    If the file exists, it will be replaced.

    :param data: Dictionary to serialize
    :param filename: Name of the JSON file
    """
    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(data, file, indent=4)

def load_and_deserialize(filename):
    """
    Loads a JSON file and deserializes it into a Python dictionary.

    :param filename: Name of the JSON file to read
    :return: Dictionary with deserialized data
    """
    with open(filename, 'r', encoding="utf-8") as file:
        return json.load(file)
