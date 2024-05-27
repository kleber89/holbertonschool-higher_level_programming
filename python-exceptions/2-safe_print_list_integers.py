#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    # Inicialice un contador para realizar un seguimiento del número de números enteros impresos
    integers_printed = 0

    # Iterar sobre los primeros x elementos de la lista.
    for i in range(x):
        try:
            # Intente imprimir el elemento actual como un número entero
            print("{:d}".format(my_list[i]), end=' ')
            integers_printed += 1
        except (ValueError, TypeError):
            # Si el elemento no se puede imprimir como un número entero, omítelo en silencio
            pass

    # Imprima una nueva línea después de imprimir todos los números enteros
    print()

    return integers_printed

# Ejemplo de uso
my_list = [1, "2", 3, "four", 5]
x = 4
num_integers_printed = safe_print_list_integers(my_list, x)
print("Number of integers printed:", num_integers_printed)
