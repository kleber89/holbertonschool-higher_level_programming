#!/usr/bin/python3
def number_keys(a_dictionary):
    # Uso len() para contar el numero de claves en el diccionario 
    num_keys = len(a_dictionary)
    return num_keys

# Ejemplo de uso
my_dictionary = {'a': 1, 'b': 2, 'c': 3}
result = number_keys(my_dictionary)
print(result)
