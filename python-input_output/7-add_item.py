#!/usr/bin/python3
"""
function that returns the dictionary description with simple data
structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object.
"""

import json
import sys
import os


def load_from_json_file(filename):
    """Reads JSON data from a file and returns the corresponding
    Python object."""
    with open(filename, 'r') as file:
        return json.load(file)


def save_to_json_file(data, filename):
    """Writes a Python object to a file in JSON format."""
    with open(filename, 'w') as file:
        json.dump(data, file)


def main():
    """Main function that loads, updates, and saves a
    list to a JSON file."""

    filename = 'add_item.json'

    # comprobar si existe
    # si no []
    if os.path.exists(filename):
        item = load_from_json_file(filename)
    else:
        item = []

    # debemos add lo dado por el usuario
    item.extend(sys.argv[1:])

    save_to_json_file(item, filename)


if __name__ == "__main__":
    main()
