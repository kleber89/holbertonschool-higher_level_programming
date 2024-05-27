#!/usr/bin/python3
def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using JSON representation."""
    json_str = to_json_string(my_obj)
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(json_str)
