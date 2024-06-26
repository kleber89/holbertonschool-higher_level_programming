#!/usr/bin/python3
"""
Rectangle that inherits from BaseGeometry 
"""


class BaseGeometry:
    """
    Class representing a base geometry with basic validation methods.
    """

    def area(self):
        """
        Method to calculate the area.

        Raises:
            Exception: Always raises an exception
            with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates if the given value is an integer greater than 0.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    Class representing a rectangle inheriting from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with width and height.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.

        Raises:
            TypeError: If width or height are not integers.
            ValueError: If width or height are less than or equal to 0.
        """
        super().__init__()  # Initialize base class (BaseGeometry)
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)
