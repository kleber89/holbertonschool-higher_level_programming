#!/usr/bin/python3
"""
returns True if the object is exactly an instance
of the specified class ; otherwise False
"""


def is_same_class(obj, a_class):
    """
    Checks if the object is exactly
    an instance of the specified class.

    Args:
        obj (object): The object to check.
        a_class (type): The class type to compare against.

    Returns:
        bool: True if obj is exactly an instance
        of a_class, otherwise False.
    """
    return type(obj) == a_class
