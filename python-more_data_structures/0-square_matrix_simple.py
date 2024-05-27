#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    squared_matrix = []

    for row in matrix:
        squared_row = []
        for num in row:
            squared_row.append(num ** 2)
        squared_matrix.append(squared_row)
    return squared_matrix

# ejemplo para usar
original_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
result_matrix = square_matrix_simple(original_matrix)
print(result_matrix)
