#!/usr/bin/python3
"""a function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    with open(filename, "r", encouding="utf_8") as file:
        for line in file:
            print(line, end="")
