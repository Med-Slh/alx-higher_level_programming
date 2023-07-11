#!/usr/bin/python3
"""a function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """fct that read a file"""
    with open(filename, "r", encoding="utf_8") as f:
        print(f.read(), end="")
