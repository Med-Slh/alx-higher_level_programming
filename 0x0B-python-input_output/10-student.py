#!/usr/bin/python3
"""class Student"""


class Student:
    """Class Student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        dict = {}
        if type(attrs) is not list:
            return self.__dict__
        else:
            for el in attrs:
                if type(el) is not str:
                    return self.__dict__
            for k in self.__dict__:
                if k in attrs:
                    dict[k] = self.__dict__[k]
        return dict
