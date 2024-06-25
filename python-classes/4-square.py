#!/usr/bin/python3


# Definition of the Square class
class Square:
    # Initializer method for the Square class
    def __init__(self, size=0):
        # Set the size using the size property (triggers validation in the setter)
        self.size = size

    # Property decorator to get the size attribute
    @property
    def size(self):
        # Return the private attribute __size
        return self.__size

    # Setter decorator to set the size attribute
    @size.setter
    def size(self, value):
        # Check if the value is not an integer
        if not isinstance(value, int):
            # If it's not an integer, raise a TypeError
            raise TypeError("size must be an integer")
        # Check if the value is less than 0
        elif value < 0:
            # If it's less than 0, raise a ValueError
            raise ValueError("size must be >= 0")
        else:
            # If it passes the checks, assign the value to the private attribute __size
            self.__size = value

    # Method to calculate the area of the square
    def area(self):
        # Return the calculated area (size squared)
        return self.__size**2
