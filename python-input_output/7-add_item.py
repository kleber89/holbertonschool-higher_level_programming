#!/usr/bin/python3
"""
Module that adds and saves all arguments to a list.
"""

import sys
from pathlib import Path
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

filename = "add_item.json"

"""
Check if the file exists, and load its content if it does
"""
if Path(filename).exists():
    items = load_from_json_file(filename)
else:
    items = []

"""
Extend the existing items list with command-line arguments
"""
items.extend(sys.argv[1:])

"""
Save the updated list back to the JSON file
"""
save_to_json_file(items, filename)
