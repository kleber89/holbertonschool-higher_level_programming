#!/usr/bin/python3
"""Empty class Square that defines a square."""


class Square:
    """Empty class Square that defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the data."""
        self.size = size
        self.position = position

    def area(self):
        """Return the area of the square."""
        return self.size * self.size

    @property
    def size(self):
        """Return the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square."""

        if not type(value) is int:
            """Raise an error if size is not an integer."""
            raise TypeError("size must be an integer")

        if value < 0:
            """Raise an error if size is less than 0."""
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """Return the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square."""

        if not type(value) is tuple or len(value) != 2:
            """Raise an error if position is not a tuple."""
            raise TypeError("position must be a tuple of 2 positive integers")

        if not type(value[0]) is int or not type(value[1]) is int:
            raise TypeError("position must be a tuple of 2 positive integers")

        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def my_print(self):
        """Print the square with the character #."""
        if self.__size > 0:
            if self.__position[1] > 0:
                print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
        else:
            print()
