#!/usr/bin/python3
"""module that add and save all arguments of a list"""
import sys
from json_file_operations import load_from_json_file, save_to_json_file


def main():
    """Main function to add command-line arguments to a JSON file."""

    # Read command-line arguments excluding the script name
    arguments = sys.argv[1:]

    # Load existing list from add_item.json (if it exists)
    try:
        existing_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        existing_list = []

    # Append new arguments to the existing list
    existing_list.extend(arguments)

    # Save the updated list back to add_item.json
    save_to_json_file(existing_list, "add_item.json")

    print(f"Added {len(arguments)} item(s) to add_item.json.")


if __name__ == "__main__":
    main()
