#!/usr/bin/python3
"""Save to JSON file"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using its JSON representation.

    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file, ensure_ascii=False, indent=4)
