#!/usr/bin/python3
"""Module that checks object instance or inherited class instance."""


def is_kind_of_class(obj, a_class):
    """Returns True if obj is instance of, or inherited from, a_class."""
    return isinstance(obj, a_class)
