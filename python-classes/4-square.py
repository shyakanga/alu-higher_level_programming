#!/usr/bin/python3
#!/usr/bin/python3
"""Module that defines a Square class using property getters and setters.

This module centralizes size validation logic using Python properties.
"""


class Square:
    """Represents a square with controlled access to private size attributes.

    Attributes:
        __size (int): The width and height dimension of the square.
    """

    def __init__(self, size=0):
        """Initializes a new Square instance.

        Args:
            size (int, optional): The size dimension of the square.
                Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the current size of the square.

        Returns:
            int: The size dimension of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square with type and value validation.

        Args:
            value (int): The new size dimension of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates and returns the current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
