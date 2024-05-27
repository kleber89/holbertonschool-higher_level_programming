#!/usr/bin/python3
def load_from_json_file(filename):
    """Creates an object from a JSON file."""
    with open(filename, 'r', encoding='utf-8') as file:
        json_str = file.read()
    return from_json_string(json_str)
