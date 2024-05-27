#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result_list = []
    for num in my_list:
        if num % 2 == 0:
            result_list.append(True)  # Si es divisible por 2 sera un True
        else:
            result_list.append(False)  # Si no se puede dividir por 2 sera un False
    return result_list
