#!/usr/bin/python3
"""Module that defines a Square class with size and 2D spatial positioning.

This module controls both dimensions and offset positioning for output.
"""


class Square:
    """Represents a square with size and 2D coordinate properties.

    Attributes:
        __size (int): The size dimension of the square.
        __position (tuple): A 2-element tuple of positive integer offsets.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new Square instance.

        Args:
            size (int, optional): Size dimension of the square. Defaults to 0.
            position (tuple, optional): (x, y) offset tuple.
                Defaults to (0, 0).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square with validation.

        Args:
            value (int): The new size dimension.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the position coordinates of the square.

        Returns:
            tuple: A tuple of 2 positive integers (x, y).
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square with validation.

        Args:
            value (tuple): A 2-element tuple containing non-negative integers.

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
        """Calculates and returns the current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square with '#' taking into account spatial position.

        If size is 0, prints an empty line. Position[1] controls vertical
        newlines (only printed if size > 0), and position[0] controls spaces.
        """
        if self.__size == 0:
            print("")
            return

        for _ in range(self.__position[1]):
            print("")

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
