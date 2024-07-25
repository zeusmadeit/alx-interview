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


# def pascal_triangle(n):

#     matrix = []

#     if n <= 0:
#         return matrix     
    
#     matrix = [[1]] 

#     for i in range(1, n):
#         temp = [1] 
#         for j in range(len(matrix[i - 1]) - 1):
#             curr = matrix[i - 1]
#             temp.append(matrix[i - 1][j] + matrix[i - 1][j + 1])
#         temp.append(1)
#         matrix.append(temp)

#     return matrix


# def print_triangle(triangle):
#     """
#     Print the triangle
#     """
#     for row in triangle:
#         print("[{}]".format(",".join([str(x) for x in row])))


# print_triangle(pascal_triangle(5))