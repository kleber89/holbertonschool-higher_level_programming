#!/usr/bin/python3
"""module json"""
import json


def to_json_string(my_obj):
    """
    Returns:
    str: The JSON representation of the object as a string.
    """
    return json.dumps(my_obj)
