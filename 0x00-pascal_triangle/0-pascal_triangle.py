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
    
    arr = [[0 for x in range(n)] for y in range(n)] 

    for row in range(0, n):
        for i in range(0, row + 1):
            if (i == 0 or i == row ):
                arr[row][i] = 1
                # print(arr[row][i], end = " ")
            else:
                arr[row][i] = (arr[row - 1][i - 1] + arr[row - 1][i])
                # print(arr[row][i], end = " ")
        # print("\n")
    return arr

