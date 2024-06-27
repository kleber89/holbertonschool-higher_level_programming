#!/usr/bin/python3
"""module that add and save all arguments of a list"""

import sys
from pathlib import Path


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
items = []

if Path(filename).exists():
    items = load_from_json_file(filename)
items.extend(sys.argv[1:])
save_to_json_file(items, filename)
