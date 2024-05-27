#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    # Inicializo un contador para llevar un seguimiento de los elementos impresos
    elements_printed = 0

    # Itero sobre los elementos de la lista
    for i in range(x):
        try:
            # Imprimo el elemento actual
            print(my_list[i], end=' ')
            # Incremento el contador
            elements_printed += 1
        except IndexError:
            # Si he impreso x los elementos, salgo del bucle
            break

    # Si IndexError ocurre, significa que hemos llegado al final de la lista
    print()

    return elements_printed

# Ejemplo de uso
my_list = [1, 2, 3, 4, 5]
x = 7
num_printed = safe_print_list(my_list, x)
print("Number of elements printed:", num_printed)
