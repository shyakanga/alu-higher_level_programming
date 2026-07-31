#!/usr/bin/python3
"""Module that defines a Square class with a private size attribute.

This module expands the Square class to encapsulate its size dimension.
"""


class Square:
    """Represents a square with a defined size.

    Attributes:
        __size (int): The width and height dimension of the square.
    """

    def __init__(self, size):
        """Initializes a new Square instance.

        Args:
            size (int): The size dimension of the square.
        """
        self.__size = size
