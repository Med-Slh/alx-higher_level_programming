#!/usr/bin/python3
"""Definition of a func that append
a string at the end of a file"""


def append_write(filename="", text=""):
    """func append a string at the of file"""
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
