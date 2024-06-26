#!/usr/bin/python3
class Square:
    """
    Class that defines a square by its size.
    """

    def __init__(self, size=0):
        """Initializes the square with an optional size parameter."""
        self.size = size  # This will use the setter to validate size

    @property
    def size(self):
        """Property to retrieve the size of the square"""
        return self._size

    @size.setter
    def size(self, value):
        """Property setter to set the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    def area(self):
        """Calculates and returns the area of the square"""
        return self._size ** 2

    def my_print(self):
        """Prints the square using the '#' character"""
        if self._size == 0:
            print()
        else:
            for _ in range(self._size):
                print("#" * self._size)
            print()
