#!/usr/bin/python3
"""Module that defines a Square class with type and value validation.

This module ensures that any assigned size is a non-negative integer.
"""


class Square:
    """Represents a square with validated size attributes.

    Attributes:
        __size (int): The width and height dimension of the square.
    """

    def __init__(self, size=0):
        """Initializes a new Square instance with optional size validation.

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
