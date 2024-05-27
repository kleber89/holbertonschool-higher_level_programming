#!#!/usr/bin/python3
def raise_exception_msg(mensaje=""):
    # Genera una excepción de nombre con el mensaje proporcionado
    raise NameError(mensaje)

# Ejemplo de uso:
try:
    raise_exception_msg("Este es un mensaje personalizado para la excepción")
except NameError as e:
    print("Se produjo un error:", e)
