#!/usr/bin/python3
"""Definition of a func that returns
num of charcters written"""


def write_file(filename="", text=""):
    """fnc that returns num of charcters written"""
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
