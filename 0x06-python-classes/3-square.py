#!/usr/bin/python3
""" A square class that define a square"""


class Square:
    """ the square class"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size     
    """Public instance that return the current squar area"""
    def area(self):
        return self.__size ** 2
