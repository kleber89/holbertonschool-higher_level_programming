#!/usr/bin/python3
def multiplicar_por_2(a_diccionario):
    # Creo un nuevo diccionario para almacenar los valores multiplicados por 2
    nuevo_diccionario = {}

    # Iteramos sobre los elementos del diccionario original
    for clave, valor in a_diccionario.items():
        # Multiplico el valor por 2 y lo asignamos a la clave correspondiente en el nuevo diccionario
        nuevo_diccionario[clave] = valor * 2

    return nuevo_diccionario

# Ejemplo de uso:
mi_diccionario = {'a': 1, 'b': 2, 'c': 3}
resultado = multiplicar_por_2(mi_diccionario)
print(resultado)
