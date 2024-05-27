#!/usr/bin/python3
def list_division(mi_lista_1, mi_lista_2, longitud_lista):
    lista_resultado = []

    try:
        for i in range(longitud_lista):
            try:
                dividendo = mi_lista_1[i]
                divisor = mi_lista_2[i]

                # Comprobamos si el dividendo y el divisor son numéricos
                if not (isinstance(dividendo, (int, float)) and isinstance(divisor, (int, float))):
                    raise TypeError("tipo incorrecto")

                # Comprobamos si el divisor no es cero
                if divisor == 0:
                    raise ZeroDivisionError("división por 0")

                # Realizamos la división
                lista_resultado.append(dividendo / divisor)

            except IndexError:
                # Manejamos el error de índice fuera de rango
                print("fuera de rango")
                lista_resultado.append(0)
            except TypeError as e:
                # Manejamos el error de tipo incorrecto
                print(e)
                lista_resultado.append(0)
            except ZeroDivisionError as e:
                # Manejamos el error de división por cero
                print(e)
                lista_resultado.append(0)

    finally:
        # Aseguramos que la lista de resultado tenga la longitud deseada
        while len(lista_resultado) < longitud_lista:
            lista_resultado.append(0)

    return lista_resultado

# Ejemplo de uso:
mi_lista_1 = [10, 20, 30]
mi_lista_2 = [5, 0, 2, 4]
longitud_lista = 5

resultado = list_division(mi_lista_1, mi_lista_2, longitud_lista)
print(resultado)
