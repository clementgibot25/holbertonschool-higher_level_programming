#!/usr/bin/python3

"""
This module provides functions to serialize and deserialize Python dictionaries to and from XML files.
"""


import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary into XML and saves it to the given filename.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The name of the file to save the XML data to.
    
    Returns:
        bool: True if serialization was successful, False otherwise.
    """
    try:
        root = ET.Element('data')
        for key, value in dictionary.items():
            child = ET.SubElement(root, str(key)) # Ensure key is string for tag
            child.text = str(value) # Ensure value is string for text
        
        tree = ET.ElementTree(root)
        tree.write(filename, encoding='utf-8', xml_declaration=True)
        return True
    except Exception:
        return False

def deserialize_from_xml(filename):
    """
    Reads XML data from a file and returns a deserialized Python dictionary.

    Args:
        filename (str): The name of the file to read XML data from.

    Returns:
        dict or None: The deserialized dictionary, or None if an error occurs.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        
        data_dict = {}
        for child in root:
            key = child.tag
            value_str = child.text
            
            # Attempt type conversion
            if value_str is None:
                data_dict[key] = None
            elif value_str.lower() == 'true':
                data_dict[key] = True
            elif value_str.lower() == 'false':
                data_dict[key] = False
            else:
                try:
                    data_dict[key] = int(value_str)
                except ValueError:
                    try:
                        data_dict[key] = float(value_str)
                    except ValueError:
                        data_dict[key] = value_str # Keep as string if no other type matches
                        
        return data_dict
    except (FileNotFoundError, ET.ParseError):
        return None
    except Exception:
        return None
