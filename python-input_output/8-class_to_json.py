#!/usr/bin/python3
"""Module that returns dictionary description for JSON serialization."""


def class_to_json(obj):
    """Returns dictionary description for JSON serialization of object."""
    return obj.__dict__
