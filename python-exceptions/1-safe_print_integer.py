#!/usr/bin/python3
def safe_print_integer(value):
    try:
        # Intento formatear e imprimir el valor como un número entero
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        # Si ocurre ValueError o TypeError, significa que el valor no se puede imprimir como un número entero
        return False

# Ejemplo de uso
value1 = 42
value2 = "Hello"

print("Value 1:")
print("Printed successfully:", safe_print_integer(value1))

print("\nValue 2:")
print("Printed successfully:", safe_print_integer(value2))

