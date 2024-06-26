#!/usr/bin/python3
"""
empty class
"""


class BaseGeometry():
    """
    Base class for geometric shapes.

    This class provides a foundation for defining various geometric shapes.
    It includes a validation function for integer values and a placeholder
    implementation of the `area()` method that raises an exception.

    Properties:
    - No properties are currently defined in the `BaseGeometry` class.

    Methods:
    - `integer_validator(self, name, value)`: Validates if the provided `value`
        is an integer greater than 0. Raises `TypeError` if `value` is not an
        integer, and `ValueError` if it's not strictly positive.
    - `area(self)`: Placeholder method that raises an `Exception` indicating
        that the specific area calculation needs to be implemented
        in subclasses.

    Raises:
    - `TypeError`: If `value` in `integer_validator` is not an integer.
    - `ValueError`: If `value` in `integer_validator` is not strictly positive.
    - `Exception`: If `area()` is called directly on the `BaseGeometry` class.

    This class is intended to be subclassed to define specific geometric shapes
    and their corresponding area calculation logic.
    """

    def integer_validator(self, name, value):
        """
        The function validates if the value is
        an integer and if it is greater than 0
        raise
            TypeError and ValueError
        """
        if type(value) is not int:
            raise (TypeError(f"{name} must be an integer"))
        if value <= 0:
            raise (ValueError(f"{name} must be greater than 0"))

    def area(self):
        """
        this fuctio returns an exception error
        """
        raise (Exception("area() is not implemented"))
        pass
