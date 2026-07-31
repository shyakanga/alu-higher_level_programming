#!/usr/bin/python3
"""Module that defines a BaseGeometry class."""


class BaseGeometry:
    """A class representing base geometry."""

    def area(self):
        """Raises an Exception indicating area is not implemented."""
        raise Exception("area() is not implemented")
