#!/usr/bin/python3
"""from JSON string"""


import json


def from_json_string(my_str):
    """
    Returns:
    object: The Python data structure represented by the JSON string.
    """
    return json.loads(my_str)
