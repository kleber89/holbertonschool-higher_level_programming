#!/usr/bin/python3
"""
class_to_json
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON serialization of an object.

    Args:
        obj: An instance of a class.

    Returns:
        A dictionary containing all serializable attributes of the object.
    """
    # Initialize an empty dictionary to store the attributes
    obj_dict = {}

    # Iterate over all attributes of the object
    for key in dir(obj):
        # Ignore private and special attributes
        if not key.startswith("__"):
            value = getattr(obj, key)
            # Check if the attribute is serializable
            if isinstance(value, (list, dict, str, int, bool)):
                obj_dict[key] = value

    return obj_dict
