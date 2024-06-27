#!/usr/bin/python3
"""Append write"""


def append_write(filename="", text=""):
    """Appends a string to a text file (UTF8)"""
    with open(filename, "a") as f:
        return f.write(text)
