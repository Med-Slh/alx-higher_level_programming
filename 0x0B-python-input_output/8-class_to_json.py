#!/usr/bin/python3
"""function that returns the dictionary description with simple
data structure for JSON serialization of an object"""


def class_to_json(obj):
    """func that returns dictionnary description"""
    return obj.__dict__
