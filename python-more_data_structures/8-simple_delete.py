#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    # Verifico si la clave está en el diccionario antes de eliminarla
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
