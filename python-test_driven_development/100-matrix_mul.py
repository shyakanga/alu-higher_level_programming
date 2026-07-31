#!/usr/bin/python3
"""Module for matrix multiplication function.

This module provides the function `matrix_mul` which validates two matrices
and computes their product.
"""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices m_a and m_b.

    Args:
        m_a (list): First matrix (list of lists of int/float).
        m_b (list): Second matrix (list of lists of int/float).

    Returns:
        list: Resulting matrix after multiplication.

    Raises:
        TypeError: If m_a or m_b is not a list, not a list of lists,
                   contains elements that are not int/float, or rows are not
                   of equal size.
        ValueError: If m_a or m_b is empty, or if m_a and m_b cannot be
                    multiplied.
    """
    # 1. Validate list type
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # 2. Validate list of lists
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # 3. Validate non-empty matrices
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    # 4. Validate elements are int or float
    for row in m_a:
        for elem in row:
            if type(elem) not in (int, float):
                raise TypeError("m_a should contain only integers or floats")

    for row in m_b:
        for elem in row:
            if type(elem) not in (int, float):
                raise TypeError("m_b should contain only integers or floats")

    # 5. Validate rectangular matrices
    row_len_a = len(m_a[0])
    for row in m_a:
        if len(row) != row_len_a:
            raise TypeError("each row of m_a must be of the same size")

    row_len_b = len(m_b[0])
    for row in m_b:
        if len(row) != row_len_b:
            raise TypeError("each row of m_b must be of the same size")

    # 6. Validate multiplication condition (cols in A == rows in B)
    if row_len_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    result = []
    for i in range(len(m_a)):
        row_result = []
        for j in range(len(m_b[0])):
            elem_sum = 0
            for k in range(len(m_b)):
                elem_sum += m_a[i][k] * m_b[k][j]
            row_result.append(elem_sum)
        result.append(row_result)

    return result
