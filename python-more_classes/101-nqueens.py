#!/usr/bin/python3
"""Module that solves the N queens problem using backtracking."""

import sys


def is_safe(board, row, col):
    """Check if placing a queen at (row, col) is safe.

    Args:
        board (list): Current queen positions as [row, col] pairs.
        row (int): Target row.
        col (int): Target column.

    Returns:
        bool: True if safe from attack, False otherwise.
    """
    for r, c in board:
        if c == col or abs(r - row) == abs(c - col):
            return False
    return True


def solve_nqueens(n, row, board):
    """Recursively finds and prints all valid N queens placements.

    Args:
        n (int): Board dimensions (N x N).
        row (int): Current row being evaluated.
        board (list): List of placed queen coordinates.
    """
    if row == n:
        print(board)
        return

    for col in range(n):
        if is_safe(board, row, col):
            board.append([row, col])
            solve_nqueens(n, row + 1, board)
            board.pop()


def main():
    """Validates CLI input and kicks off the N queens solver."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(n, 0, [])


if __name__ == "__main__":
    main()
