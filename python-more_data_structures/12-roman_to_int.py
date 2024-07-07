#!/usr/bin/python3

def roman_to_int(roman_str):
    roman_to_decimal = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    roman_str = roman_str.upper()
    n = len(roman_str)

    decimal_values = []

    for char in roman_str:
        if char in roman_to_decimal:
            decimal_values.append(roman_to_decimal[char])
        else:
            raise ValueError(f"invalid: {char}")

    total = 0
    for i in range(n - 1):
        if decimal_values[i] < decimal_values[i + 1]:
            total -= decimal_values[i]
        else:
            total += decimal_values[i]

    total += decimal_values[-1]

    return total
