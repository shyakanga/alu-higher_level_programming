#!/usr/bin/python3
"""Module providing the MagicClass built from dissembled bytecode.

This module reproduces the behavior of circle calculations matching
specific Python instructions.
"""

import math


class MagicClass:
    """Represents a circle with area and circumference methods."""

    def __init__(self, radius=0):
        """Initializes a MagicClass instance with radius validation.

        Args:
            radius (int or float, optional): Circle radius. Defaults to 0.

        Raises:
            TypeError: If radius is not an int or float.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Calculates the circle area.

        Returns:
            float: Computed area.
        """
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """Calculates circle circumference.

        Returns:
            float: Computed circumference.
        """
        return 2 * math.pi * self.__radius
