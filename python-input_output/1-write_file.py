#!/usr/bin/python3
"""Module that contains a function to write to a text file."""


def write_file(filename="", text=""):
    """Writes a string to a text file and returns characters written."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
