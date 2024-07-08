#!/usr/bin/python3
"""
Class BaseGeometry
"""


class BaseGeometry:
    """
    A class used to represent the base geometry
    """

    def area(self):
        """
        Public instance method that raises an exception for area that is
        not implemented.

        Raises:
            Exception: Indicates that the method is not implemented.
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Public instance method that validates the value as an integer.

        Args:
            name (str): The name of the parameter.
            value (int): The value to be validated.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
