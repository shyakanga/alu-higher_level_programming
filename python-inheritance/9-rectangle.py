#!/usr/bin/python3
"""Module that defines a Rectangle class with area and str representation."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class representing a rectangle."""

    def __init__(self, width, height):
        """Initializes width and height after validation."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns string representation of the rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
