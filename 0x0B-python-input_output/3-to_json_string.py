#!/usr/bin/python3
"""func that returns the JSON representation of an object"""
import json


def to_json_string(my_obj):
    """a function that return json representation"""
    return json.dumps(my_obj)
