#!/usr/bin/python3
"""Program that returns a list of lists"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal's triangle
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            """Append the sum of the two elements."""
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle
