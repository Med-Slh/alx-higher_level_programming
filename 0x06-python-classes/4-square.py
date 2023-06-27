#!/usr/bin/python3
""" A square class that define a square"""


class Square:
    """ the square class"""

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """the ccurrent size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Public instance that return the current squar area"""
        return (self.__size * self.__size)
