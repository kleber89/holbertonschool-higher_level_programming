#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    # Actualiza o agrega la clave/valor al diccionario
    a_dictionary[key] = value

# Ejemplo de uso
my_dictionary = {'a': 1, 'b': 2, 'c': 3}
key = 'b'
value = 5

update_dictionary(my_dictionary, key, value)
print(my_dictionary)
