#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Uso de conjunto para el seguimiento de los numeros enteros unicos
    unique_integers = set()

    # Iterateracion de la lista y add de los nnumeros enteros
    for num in my_list:
        unique_integers.add(num)

    # Suma de todos los numeros enteros
    sum_unique = sum(unique_integers)

    return sum_unique

# Ejemplo de uso
my_list = [1, 2, 2, 3, 4, 4, 5]
result = uniq_add(my_list)
print(result)
