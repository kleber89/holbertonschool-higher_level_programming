#!/usr/bin/python3
"""Module that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a list of lists")

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a list of lists")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix of integers/floats")

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a list of lists")

    row_size = len(matrix[0])

    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        new_matrix.append(new_row)

    return new_matrix