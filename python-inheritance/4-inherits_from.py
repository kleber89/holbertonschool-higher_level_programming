#!/usr/bin/python3
"""
function determines whether an object was inherited or not
"""


def inherits_from(obj, a_class):
    """
    Checks if the object is an instance of
    a class that inherited (directly or indirectly)
    from the specified class.

    Args:
        obj (object): The object to check.
        a_class (type): The class type to compare against.

    Returns:
        bool: True if obj is an instance
        of a class that inherits from a_class,
              otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
