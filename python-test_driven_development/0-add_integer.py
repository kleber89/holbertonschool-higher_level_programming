#!/usr/bin/python3
"""Function that adds 2 integers.
a and b must be first casted to integers if they are float
a and b must be integers or floats, otherwise raise a TypeError
Returns an integer: the addition of a and b
"""


def add_integer(a, b=98):
    """
    Function that adds 2 integers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b