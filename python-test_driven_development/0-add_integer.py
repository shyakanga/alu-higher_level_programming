#!/usr/bin/python3
"""
This module contains a function that adds two integers.
"""


def add_integer(a, b=98):
    """
    Adds 2 integers or floats casted to integers.

    Args:
        a: first integer or float
        b: second integer or float (default 98)

    Returns:
        The addition of a and b as an integer
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
