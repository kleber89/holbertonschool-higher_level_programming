#!/usr/bin/python3
"""module json"""
import json


def to_json_string(my_obj):
    """
    Converts an object (dictionary or list) into its JSON representation as a string.

    Parameters:
    my_obj (object): The object to be converted to JSON.

    Returns:
    str: The JSON representation of the object as a string.
    """
    return json.dumps(my_obj)
