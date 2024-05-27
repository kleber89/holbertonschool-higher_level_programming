#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # Calculo la diferencia entre set_1 y set_2
    diff_set_1 = set_1.symmetric_difference(set_2)

    return diff_set_1

# Ejemplo de uso
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 5, 6, 7, 8}

result = only_diff_elements(set_1, set_2)
print(result)
