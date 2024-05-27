def add_integer(a, b=98):
    """
    Suma dos números enteros.

    Args:
        a: El primer número, debe ser un entero o un flotante.
        b: El segundo número, debe ser un entero o un flotante. Por defecto es 98.

    Returns:
        La suma de a y b como un número entero.

    Raises:
        TypeError: Si a o b no son enteros ni flotantes.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a debe ser un número entero")
    if not isinstance(b, (int, float)):
        raise TypeError("b debe ser un número entero")

    # Convertir a y b a enteros si son flotantes
    a = int(a)
    b = int(b)

    return a + b

# Ejemplos de uso
print(add_integer(10, 20))  # 30
print(add_integer(10.5, 20))  # 30
print(add_integer(10))  # 108
