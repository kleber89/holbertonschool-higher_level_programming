#!/usr/bin/python3
"""
Lookup
"""


def lookup(obj):
    """
    Returns the list of available attributes
    and methods of an object.

    Args:
        obj (object): The object for which to
        retrieve attributes and methods.

    Returns:
        list: A sorted list of strings representing
        attributes and methods of the object.
    """
    return sorted(dir(obj))
