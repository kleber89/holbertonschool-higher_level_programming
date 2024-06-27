#!/usr/bin/python3
"""Append write"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a UTF-8 encoded text file and returns the number of characters added.

    Parameters:
    filename (str): The name of the file to append to (default is an empty string).
    text (str): The string to append to the file (default is an empty string).

    Returns:
    int: The number of characters added to the file.

    """
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)
        return len(text)
