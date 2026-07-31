#!/usr/bin/python3
"""
This module contains the function add_integer.
"""


def add_integer(a, b=98):
    """Adds two integers or floats converted to integers.

    Args:
        a: First number (int or float).
        b: Second number (int or float, default 98).

    Returns:
        The sum of a and b as an integer.

    Raises:
        TypeError: If a or b is not an integer/float, or is NaN/infinity.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    try:
        a = int(a)
    except (OverflowError, ValueError):
        raise TypeError("a must be an integer")

    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    try:
        b = int(b)
    except (OverflowError, ValueError):
        raise TypeError("b must be an integer")

    return a + b
