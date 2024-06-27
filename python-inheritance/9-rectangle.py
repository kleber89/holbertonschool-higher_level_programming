#!/usr/bin/python3
"""
empty class
"""

class BaseGeometry:
    def area(self):
        """Raises an error if area method is not implemented."""
        raise NotImplementedError("area() is not implemented")
    
    def integer_validator(self, name, value):
        """Validates that the value is an integer greater than 0."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """Initializes a Rectangle instance with width and height."""
        super().__init__()
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns a string representation of the rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"