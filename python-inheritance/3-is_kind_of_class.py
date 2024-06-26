#!/usr/bin/python3
"""
function determines whether an object was inherited or not
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if the object is an instance
    of, or if it is an instance of a class
    that inherited from, the specified class.

    Args:
        obj (object): The object to check.
        a_class (type): The class type to compare against.

    Returns:
        bool: True if obj is an instance
        of a_class or inherits from it, otherwise False.
    """
    return isinstance(obj, a_class)
