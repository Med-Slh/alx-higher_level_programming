#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        lenrow = len(row)
        for i in range(lenrow):
            print("{:d}".format(row[i]), end='')
            if i < lenrow - 1:
                print("{}".format(' '), end='')
        print()
