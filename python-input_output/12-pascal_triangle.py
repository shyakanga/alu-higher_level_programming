#!/usr/bin/python3
"""Module that defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Return a list of lists of integers representing Pascal's triangle."""
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        prev = triangle[-1]
        curr = [1]
        for i in range(len(prev) - 1):
            curr.append(prev[i] + prev[i + 1])
        curr.append(1)
        triangle.append(curr)
    return triangle
