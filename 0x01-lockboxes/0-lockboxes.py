#!/usr/bin/python3
"""Lockboxes - alx interview prep project
"""
from typing import List


def canUnlockAll(boxes: List[List[int]]) -> bool:
    """Determines if all the boxes can be opened,
    the first box - boxes[0] is unlocked.

    Arguments:
    boxes (List[list]): is a list of lists

    Return: Returns True if all boxes can be opened, else return False.
    """
    keys = {0}

    for key, box in enumerate(boxes):

        if key not in keys:
            return False

        for val in box:
            keys.update(boxes[val])

        keys.update(boxes[key])

    return True
