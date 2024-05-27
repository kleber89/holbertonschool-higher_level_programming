#!/usr/bin/python3
def best_score(a_dictionary):
    # Inicializo variables para realizar un seguimiento de la mejor puntuación y su clave correspondiente
    best_key = None
    best_score = float('-inf')  # Inicialice con infinito negativo para garantizar que se considere cualquier valor en el diccionario.

    # Itero sobre los elementos del diccionario.
    for key, value in a_dictionary.items():
        # Compruebo si el valor actual es mayor que la mejor puntuación actual
        if value > best_score:
            best_score = value
            best_key = key

    return best_key

# Ejemplo de uso
my_dictionary = {'a': 85, 'b': 92, 'c': 78, 'd': 95}
result = best_score(my_dictionary)
print(result)
