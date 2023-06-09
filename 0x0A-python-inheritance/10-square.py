#!/usr/bin/python3
"""class Square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""
    def __init__(self, size):
        """constructure to initialis"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
