#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    return list(map(lambda x: x * number, my_list))

# Ejemplo de uso
original_list = [1, 2, 3, 4, 5]
multiplied_list = multiply_list_map(original_list, 2)
print(multiplied_list)
