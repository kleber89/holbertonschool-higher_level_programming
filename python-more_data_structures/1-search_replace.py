#!/usr/bin/python3
def search_replace(my_list, buscar, reemplazar):

    nueva_lista = []
    for elemento in my_list:

        if elemento == buscar:
            nueva_lista.append(reemplazar)
        else:
            nueva_lista.append(elemento)
    return nueva_lista

# Ejemplo de uso:
lista_original = [1, 2, 3, 4, 5, 2]
elemento_buscar = 2
elemento_reemplazar = 9

resultado = search_replace(lista_original, elemento_buscar, elemento_reemplazar)
print(resultado)
