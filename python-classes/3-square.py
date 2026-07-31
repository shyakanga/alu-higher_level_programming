#!/usr/bin/python3
"""Module that defines a Square class capable of computing its area.

This module adds area calculation functionality to the Square class.
"""


class Square:
    """Represents a square and provides area computation functionality.

    Attributes:
        __size (int): The width and height dimension of the square.
    """

    def __init__(self, size=0):
        """Initializes a new Square instance with size validation.

        Args:
            size (int, optional): The size dimension of the square.
                Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates and returns the current square area.

        Returns:
            int: The area of the square (size multiplied by size).
        """
        return self.__size ** 2
