#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):

    result = []
    for i in range(list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
            result.append(div)
        except ZeroDivisionError:
            div = 0
            result.append(div)
            print("division by 0")
        except IndexError:
            div = 0
            result.append(div)
            print("out of range")
        except (TypeError, ValueError):
            div = 0
            result.append(div)
            print("wrong type")
        finally:
            pass
    return result
