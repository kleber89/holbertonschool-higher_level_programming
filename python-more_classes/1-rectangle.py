#!/usr/bin/python3
class Rectangle:
    """
    This class defines a rectangle by its width and height.

    Attributes:
        width (int): Width of the rectangle.
        height (int): Height of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle object with optional width and height.

        Args:
            width (int): Width of the rectangle (default is 0).
            height (int): Height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter method for retrieving the width of the rectangle.

        Returns:
            int: Width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for setting the width of the rectangle.

        Args:
            value (int): Width value to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for retrieving the height of the rectangle.

        Returns:
            int: Height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for setting the height of the rectangle.

        Args:
            value (int): Height value to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
