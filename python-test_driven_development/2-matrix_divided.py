#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.
    Args:
        matrix: A list of lists of integers or floats.
        div: The divisor, must be an integer or float.
    Returns:
        A new matrix with all elements divided by div, rounded to 2 decimal places.
    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
                   If each row of the matrix is not of the same size.
                   If div is not an integer or float.
        ZeroDivisionError: If div is equal to 0.
    """
    if not (isinstance(matrix, list) and all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats"
                )

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide all elements of the matrix by div and round to 2 decimal places
    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]
    return new_matrix