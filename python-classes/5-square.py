#!/usr/bin/python3
class Square:
    """
    Class that defines a square by its size.
    """

    def __init__(self, size=0):
        """
        Initializes the square with an optional size parameter.
        Args:
            size (int): The size of the square, default is 0.
        """
        self.size = size  # This will use the setter to validate size

    @property
    def size(self):
        """
        Property to retrieve the size of the square.
        Returns:
            int: The size of the square.
        """
        return self._size

    @size.setter
    def size(self, value):
        """
        Property setter to set the size of the square.
        Args:
            value (int): The size value to set.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    def area(self):
        """
        Calculates and returns the area of the square.
        Returns:
            int: The area of the square.
        """
        return self._size ** 2

    def my_print(self):
        """
        Prints the square using the '#' character.
        If size is 0, prints an empty line.
        """
        if self._size == 0:
            print()
        else:
            for _ in range(self._size):
                print("#" * self._size)
            print()
