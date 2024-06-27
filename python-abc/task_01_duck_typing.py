#!/usr/bin/python3

from abc import ABC, abstractmethod

"""
class of Animal
"""
import math


class Shape(ABC):
    """
    Shape is an abstract base class that
    defines the blueprint for its subclasses.
    It contains two abstract methods: area and perimeter.
    """

    @abstractmethod
    def area(self):
        """
        Abstract method to be implemented by subclasses.
        Should return the area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Abstract method to be implemented by subclasses.
        Should return the perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    Circle is a subclass of Shape.
    It implements the area and perimeter methods.
    The constructor accepts a radius.
    """

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """
        Returns the area of the circle.
        """
        return math.pi * self.radius**2

    def perimeter(self):
        """
        Returns the perimeter (circumference) of the circle.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Rectangle is a subclass of Shape.
    It implements the area and perimeter methods.
    The constructor accepts the width and height.
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """
        Returns the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Returns the perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Prints the area and perimeter of the shape.
    This function relies on duck typing to
    call the area and perimeter methods of the shape.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
