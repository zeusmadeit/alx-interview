#!/usr/bin/env/python
"""
Implementing Pascal's Triangle in Python
"""
from typing import List


def pascal_triangle(n: int) -> List[List]:
    """
    Returns a list of lists of integers
    representing the Pascal's triangle of n.
    """
    if n <= 0:
        return []
    
    # empty matrix generated to store pascal triangle
    matrix = []

    for row in range(0, n):
        temp = []
        for col in range(0, row + 1):
            if (col == 0 or col == row ):
                temp.append(1)
            else:
                temp.append(matrix[row - 1][col - 1] + matrix[row - 1][col])
        matrix.append(temp)

    return matrix
