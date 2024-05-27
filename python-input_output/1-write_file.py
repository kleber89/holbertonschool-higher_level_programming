#!/usr/bin/python3
def escribir_archivo(nombre_archivo="", texto=""):
    """Escribe una cadena en un archivo de texto UTF-8 y devuelve el número de caracteres escritos."""
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        caracteres_escritos = archivo.write(texto)
    return caracteres_escritos
