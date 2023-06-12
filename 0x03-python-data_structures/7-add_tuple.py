#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    lenta = len(tuple_a)
    lentb = len(tuple_b)
    if lenta < 2:
        if lenta == 0:
            tuple_a = 0, 0
        else:
            tuple_a = tuple_a[0], 0
    if lentb < 2:
        if lentb == 0:
            tuple_b = 0, 0
        else:
            tuple_b = tuple_b[0], 0
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
