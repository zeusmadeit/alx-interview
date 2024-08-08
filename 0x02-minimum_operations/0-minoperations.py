#!/usr/bin/python3
"""Minimum Operations - An alx interview prep project"""


def minOperations(n: int) -> int:
    """Given a number n, this function calculates the
    fewest number of operations needed to result in 
    exactly n 'H' characters in the file

    Arguments:
    n (int): a number

    Return: Returns an integer, If n is impossible to achieve it returns 0
    """
    min_operations = 0
    char_len = 1
    clipboard = 0

    if n <= 1:
        return 0

    while char_len < n:
        # If char_len is a factor of n or char_len == 1, we copy all
        if n % char_len == 0:
            clipboard = char_len
            min_operations += 1

        char_len += clipboard
        min_operations += 1
    
    return min_operations
