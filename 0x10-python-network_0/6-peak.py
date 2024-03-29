#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module defines find_peak function.

Example:
    print(find_peak([1, 2, 4, 6, 3]))

"""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers.
    Args:
        list_of_integers (list): integers to be used.
    Returns:
        peak element.
    """

    my_list = list_of_integers
    if my_list is None or len(my_list) == 0:
        return None

    if len(my_list) == 1 or my_list[0] > my_list[1]:
        return my_list[0]

    start = 0
    end = len(my_list) - 1
    while start < end:
        mid = start + (end - start) // 2
        if my_list[mid] > my_list[mid - 1] and my_list[mid] > my_list[mid + 1]:
            return my_list[mid]
        if my_list[mid - 1] > my_list[mid + 1]:
            end = mid
        else:
            start = mid + 1
    return my_list[start]
