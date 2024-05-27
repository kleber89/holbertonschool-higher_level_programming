#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        # Intentar realizar la división
        resultado = a / b
    except ZeroDivisionError:
        # Manejar el error de división por cero
        print("Error: División por cero")
        return None
    except TypeError:
        # Manejar el error si b no es un número
        print("Error: El divisor no es un número")
        return None
    except Exception as e:
        # Manejar otras excepciones
        print("Se produjo un error:", e)
        return None
    else:
        # Si no ocurrió ninguna excepción, imprimir el resultado
        print("Resultado interno: {}".format(resultado))
        return resultado
    finally:
        # Este bloque se ejecuta siempre, independientemente de si ocurrió una excepción o no
        print("Bloque finally ejecutado")

# Ejemplo de uso:
resultado = safe_print_division(10, 2)
print("Resultado:", resultado)

resultado = safe_print_division(10, 0)
print("Resultado:", resultado)

resultado = safe_print_division("10", 2)
print("Resultado:", resultado)
