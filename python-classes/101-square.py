#!/usr/bin/python3
"""Module that defines a Square class printable with print().

This module allows printing a Square instance directly using __str__.
"""


class Square:
    """Represents a square with printable representation.

    Attributes:
        __size (int): Size dimension of the square.
        __position (tuple): (x, y) 2D offset coordinate.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new Square instance.

        Args:
            size (int, optional): Size of square. Defaults to 0.
            position (tuple, optional): Spatial offset. Defaults to (0, 0).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves size of the square.

        Returns:
            int: The size dimension.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets size dimension with type and value validation.

        Args:
            value (int): Size dimension.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves position coordinate tuple.

        Returns:
            tuple: (x, y) coordinate pair.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets position tuple with validation.

        Args:
            value (tuple): 2-element tuple of positive integers.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not isinstance(value[0], int) or
                not isinstance(value[1], int) or
                value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates area of the square.

        Returns:
            int: Calculated area.
        """
        return self.__size ** 2

    def my_print(self):
        """Prints square with '#' considering position offsets."""
        print(self.__str__())

    def __str__(self):
        """Defines string representation of the Square instance.

        Returns:
            str: Visual representation with '#' characters.
        """
        if self.__size == 0:
            return ""

        res = []
        for _ in range(self.__position[1]):
            res.append("")

        for _ in range(self.__size):
            res.append(" " * self.__position[0] + "#" * self.__size)

        return "\n".join(res)
