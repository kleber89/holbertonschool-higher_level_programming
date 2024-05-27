#!/usr/bin/python3
def read_file(filename=""):
    """Lee un archivo de texto en UTF-8 e imprime su contenido en stdout."""
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read())
