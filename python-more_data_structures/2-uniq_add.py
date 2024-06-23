#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_numbers = set()
    for num in my_list:
        unique_numbers.add(num)
        sum_unique = sum(unique_numbers)

    return sum_unique
