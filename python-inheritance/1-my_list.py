#!/usr/bin/python3
"""Module that defines a MyList class."""


class MyList(list):
    """Class that inherits from list with a sorted print method."""

    def print_sorted(self):
        """Prints the list in ascending sorted order."""
        print(sorted(self))
