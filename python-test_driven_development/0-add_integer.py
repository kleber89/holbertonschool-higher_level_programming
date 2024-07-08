#!/usr/bin/python3
"""
Adds two integers (or one and a default of 98).
Raises TypeError for non-numeric input.
"""


def add_integer(a, b=98):
    """
    Adds two integers together.

    This function takes two arguments, `a` and `b`, and returns their sum.
    If only one argument is provided, the default value of `b` (which is 98)
    is used as the second operand.

    Args:
        a (int): The first number to be added.
        b (int, optional): The second number to be added. Defaults to 98.

    Returns:
        int: The sum of `a` and `b`.

    Raises:
        TypeError: If either `a` or `b` is not an integer or a float.
    """
    if type(a) not in [float, int]:
        raise TypeError("a must be an integer")
    if type(b) not in [float, int]:
        raise TypeError("b must be an integer")
    if a is float('inf'):
        raise OverflowError('cannot convert float infinity to integer')
    if b is float('inf'):
        raise OverflowError('cannot convert float infinity to integer')
    return int(a + b)
