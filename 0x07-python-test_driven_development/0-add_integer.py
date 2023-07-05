#!/usr/bin/python3
"""Definition for a function that add two integers"""


def add_integer(a, b=98):
    """Function that adds two integers
    Returns:
        int: the result of a + b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
