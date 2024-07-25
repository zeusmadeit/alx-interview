#!/usr/bin/env/python
"""
Implementing Pascal's Triangle in Python
"""
from typing import List


def pascal_triangle(n: int) -> List:
    """
    Returns a list of lists of integers
    representing the Pascal's triangle of n.
    """
    matrix = [] # empty matrix to store pascal triangle

    if n <= 0:
        return []

    for row in range(0, n):
        temp = []
        for col in range(0, row + 1):
            if (col == 0 or col == row ):
                temp.append(1)
            else:
                temp.append(matrix[row - 1][col - 1] + matrix[row - 1][col])
        matrix.append(temp)

    return matrix


# def print_triangle(triangle):
#     """
#     Print the triangle
#     """
#     for row in triangle:
#         print("[{}]".format(",".join([str(x) for x in row])))


# print_triangle(pascal_triangle(5))