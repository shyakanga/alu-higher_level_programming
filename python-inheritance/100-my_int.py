#!/usr/bin/python3
"""Module defining a rebel integer class MyInt."""


class MyInt(int):
    """Class MyInt that inherits from int with inverted == and != operators."""

    def __eq__(self, other):
        """Inverts equality operator."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Inverts inequality operator."""
        return super().__eq__(other)
