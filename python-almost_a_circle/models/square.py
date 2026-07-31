#!/usr/bin/python3
"""Defines the Square class, which inherits from Rectangle."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square, inherits from Rectangle.

    A Square is a special Rectangle whose width and height are
    always equal, managed together through the size attribute.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square instance.

        Args:
            size (int): The size (width and height) of the Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """int: The size of the Square (its width and height)."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Return the string representation of the Square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Update attributes via no-keyword or keyword arguments.

        Args:
            *args: New attribute values, applied in order to id,
                size, x, and y.
            **kwargs: New attribute values as key/value pairs,
                where each key is an attribute name. This is
                skipped entirely if args is not empty.
        """
        if args and len(args) > 0:
            attrs = ["id", "size", "x", "y"]
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
