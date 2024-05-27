#!/usr/bin/python3
def leer_archivo(nombre_archivo=""):
    """Lee un archivo de texto en UTF-8 e imprime su contenido en stdout."""
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        print(archivo.read())
