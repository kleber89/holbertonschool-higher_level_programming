#!/usr/bin/python3
"""
empty class
"""


class BaseGeometry:
    """
    Empty class representing a base geometry.

    This class can be used as a base class for
    defining geometry-related operations
    and properties in derived classes.
    """

    def area(self):
        """
        Method to calculate the area.

        Raises:
            Exception: Always raises an exception with
            the message 'area() is not implemented'.
        """
        raise Exception('area() is not implemented')
