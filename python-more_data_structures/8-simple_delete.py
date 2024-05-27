#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    # Verifico si la clave está en el diccionario antes de eliminarla
    if key in a_dictionary:
        del a_dictionary[key]

# Ejemplo de uso:
mi_diccionario = {'a': 1, 'b': 2, 'c': 3}
clave_a_eliminar = 'b'

simple_delete(mi_diccionario, clave_a_eliminar)
print(mi_diccionario)
