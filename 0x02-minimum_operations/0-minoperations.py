#!/usr/bin/python3
"""Minimum Operations - An alx interview prep project.

Approach:
1. find the prime factors of n and save them to a list n_factors, create a variable steps = 0
2. copy and paste 'H' (2 operations, update step += 2) then keep pasting, increasing steps each time 
till the character length equals the smallest factor of n.
3. now copy and paste the characters in the file
4. check if the new character length is a factor of n
5. if not, paste and perform step 4 again
6. if true, perform step 3 again
7. return steps
"""
from typing import List


def get_factors(n: int) -> List:
    """gets the factors of n"""
    factors = []
    for x in range(2, n):
        if n % x == 0:
            factors.append(x)

    return factors


def minOperations(n: int) -> int:
    """Given a number n, this function calculates the
    fewest number of operations needed to result in 
    exactly n 'H' characters in the file

    Arguments:
    n (int): a number

    Return: Returns an integer, If n is impossible to achieve it returns 0
    """
    factors = get_factors(n)
    print(f"factors are {factors}")
    steps = 0
    char_len = 1

    if n <= 1:
        return 0
    else:
        char_len += 1
        steps += 2

    while char_len != n:
        if char_len in factors:
            char_len = char_len * 2
            steps += 2
            continue

        char_len += 1
        steps += 1
    
    return steps


if __name__ == "__main__":
    res = minOperations(12)
    print(res)
