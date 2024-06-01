#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    # Verificar si el índice es negativo o está fuera del rango de la lista
    if idx < 0 or idx >= len(my_list):
        return my_list[:]
    # Eliminar el elemento en el índice especificado
    del my_list[idx]

    return new_list
