#!/usr/bin/python3
""" a square class that define a square"""


class Square:
    """ the new square"""

    def __init__(self, size=0):
        """create a new instance"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
