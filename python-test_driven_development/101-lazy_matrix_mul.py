#!/usr/bin/python3
"""
This module contains the function lazy_matrix_mul.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies 2 matrices by using NumPy.

    Args:
        m_a: First matrix.
        m_b: Second matrix.

    Returns:
        The matrix product of m_a and m_b.
    """
    return np.matmul(m_a, m_b)
