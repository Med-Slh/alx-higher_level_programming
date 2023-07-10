#!/usr/bin/python3
""" a class MyList that inherits from list"""


class MyList(list):
    """a class MyList inherits from the class list"""
    def print_sorted(self):
        """a function that return a sorted the list"""
        print(sorted(self))
