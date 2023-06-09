#!/usr/bin/python3
"""Definition for a function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """ function that divides all elements of a matrix

    Returns:
        new matrix: a new matrix
    """
    new_matrix = []
    size_first_el = len(matrix[0])
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    for el in matrix:
        if not isinstance(el, list):
            raise TypeError(msg)
        if len(el) != size_first_el:
            raise TypeError("Each row of the matrix must have the same size")
        for subel in el:
            if not isinstance(subel, (int, float)):
                raise TypeError(msg)
        if not isinstance(div, (int, float)):
            raise TypeError("div must be a number")
        if div == 0:
            raise ZeroDivisionError("division by zero")
        new_row = [round(sub/div, 2) for sub in el]
        new_matrix.append(new_row)
    return new_matrix
