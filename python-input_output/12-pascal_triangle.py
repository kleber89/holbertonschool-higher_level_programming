#!/usr/bin/python3
"""Program that returns a list of lists"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle of n.

    Args:
        n (int): The number of rows in Pascal's Triangle.

    Returns:
        list: A list of lists of integers representing Pascal's Triangle.
    """
    # Handle the case where n is less than or equal to 0
    if n <= 0:
        return []

    # Initialize the Pascal's Triangle with the first row
    triangle = [[1]]

    # Generate each row of the triangle
    for i in range(1, n):
        # Start the new row with 1
        row = [1]

        # Compute the inner elements of the row
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

        # End the row with 1
        row.append(1)

        # Append the new row to the triangle
        triangle.append(row)

    return triangle
