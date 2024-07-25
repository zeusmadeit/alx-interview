#!/usr/bin/python3
"""
Implementing Pascal's Triangle in Python
"""

def pascal_triangle(n):
    """
    Returns a list of lists of integers
    representing the Pascal's triangle of n.
    """
    matrix = []

    if n <= 0:
        return matrix

    for row in range(0, n):
        temp = []
        for col in range(0, row + 1):
            if (col == 0 or col == row ):
                temp.append(1)
            else:
                temp.append(matrix[row - 1][col - 1] + matrix[row - 1][col])
        matrix.append(temp)

    return matrix
