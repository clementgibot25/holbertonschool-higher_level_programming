#!/usr/bin/python3
"""
Module for deleting dictionary keys with a specific value
"""

def complex_delete(a_dictionary, value):
    """
    Deletes keys with a specific value in a dictionary.
    
    Args:
        a_dictionary (dict): The input dictionary
        value: The value to search for and delete
        
    Returns:
        dict: The modified dictionary with keys removed
    """
    # Create a list of keys to delete (to avoid modifying dict during iteration)
    keys_to_delete = [k for k, v in a_dictionary.items() if v == value]
    
    # Delete each key that has the specified value
    for key in keys_to_delete:
        del a_dictionary[key]
        
    return a_dictionary
