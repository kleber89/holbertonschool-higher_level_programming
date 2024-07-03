#!/usr/bin/python3
"""
the script  adds all arguments to
a Python list, and then save them to a file
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    """
    Adds command line arguments to a list, saves it as JSON to add_items.json.
    """

    arguments = sys.argv[1:]

    try:
        data = load_from_json_file("add_item.json")
    except FileNotFoundError:
        data = []

    data.extend(arguments)

    save_to_json_file("add_item.json", data)

    print(f"Saved {len(data)} items to add_item.json")


if __name__ == "__main__":
    main()
