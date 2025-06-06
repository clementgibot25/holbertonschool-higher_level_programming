#!/usr/bin/python3
"""
This module defines a class CustomObject that can be serialized
and deserialized using the pickle module.
"""


import pickle

class CustomObject:
    """A custom object with name, age, and student status."""
    def __init__(self, name: str, age: int, is_student: bool):
        """Initializes a CustomObject instance.

        Args:
            name (str): The name of the object.
            age (int): The age of the object.
            is_student (bool): The student status of the object.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Displays the attributes of the object."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename: str):
        """Serializes the current instance and saves
        it to the provided filename.

        Args:
            filename (str): The name of the file to save the object to.

        Returns:
            None
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except (IOError, pickle.PicklingError) as e:
            # print(f"Error serializing object to {filename}: {e}") # Optional: for debugging
            return None

    @classmethod
    def deserialize(cls, filename: str):
        """Loads and returns an instance of CustomObject from the provided filename.

        Args:
            filename (str): The name of the file to load the object from.

        Returns:
            CustomObject or None: The deserialized object, or None if an error occurs.
        """
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except (IOError, pickle.UnpicklingError, EOFError, AttributeError, ImportError, IndexError) as e:
            # print(f"Error deserializing object from {filename}: {e}") # Optional: for debugging
            return None
