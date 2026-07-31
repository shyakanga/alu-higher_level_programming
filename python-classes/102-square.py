#!/usr/bin/python3
"""Module that defines a Square class with area comparison operators.

This module supports rich comparison operators based on square area.
"""


class Square:
    """Represents a square capable of area comparison operators.

    Attributes:
        __size (float or int): Size dimension of the square.
    """

    def __init__(self, size=0):
        """Initializes a new Square instance.

        Args:
            size (float or int, optional): Size of square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """Retrieves size dimension.

        Returns:
            float or int: Size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets size dimension with validation.

        Args:
            value (float or int): Size dimension.

        Raises:
            TypeError: If value is not a number.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates current square area.

        Returns:
            float or int: Calculated area.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """Equal comparison by area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Not equal comparison by area."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Less than comparison by area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Less than or equal comparison by area."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Greater than comparison by area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Greater than or equal comparison by area."""
        return self.area() >= other.area()
