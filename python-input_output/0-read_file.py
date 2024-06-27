#!/usr/bin/python3
"""Read file"""


def read_file(filename=""):
    """
    Reads a UTF-8 encoded text file and prints its contents to stdout.

    Parameters:
    filename (str): The name of the file to read (default is an empty string).

    """
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")
