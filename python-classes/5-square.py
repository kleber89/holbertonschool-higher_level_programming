#!/usr/bin/python3
"""Empty class Square that defines a square."""


class Square:
    """Empty class Square that defines a square."""

    def __init__(self, size=0):
        """Initializes the data."""
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

    @property
    def size(self):
        """Return the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        self.__size = value

        if not type(self.__size) is int:
            """Raise an error if size is not an integer."""
            raise TypeError("size must be an integer")

        if self.__size < 0:
            """Raise an error if size is less than 0."""
            raise ValueError("size must be >= 0")

    def my_print(self):
        """Print the square with the character #."""
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end="")
                print()
