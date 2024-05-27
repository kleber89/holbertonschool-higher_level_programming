#!#!/usr/bin/python3
def raise_exception():
    # Generamos una excepción de tipo
    raise TypeError("Esto es una excepción de tipo")

# Ejemplo de uso:
try:
    raise_exception()
except TypeError as e:
    print("Se produjo un error:", e)
