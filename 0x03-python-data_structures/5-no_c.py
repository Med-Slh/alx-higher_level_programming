#!/usr/bin/python3
def no_c(my_string):
    newstr = ""
    for el in my_string:
        if el != "c" and el != 'C':
            newstr += el
    return newstr
