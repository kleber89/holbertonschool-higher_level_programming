#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # optención de las claves en el diccionario de manera ordenada
    sorted_keys = sorted(a_dictionary.keys())

    # Itero las claves ordenadas para inprimir los pares clave-valor
    for key in sorted_keys:
        print(f'{key}: {a_dictionary[key]}')

# Ejemplo de uso
my_dictionary = {'b': 2, 'a': 1, 'c': 3}
print_sorted_dictionary(my_dictionary)
