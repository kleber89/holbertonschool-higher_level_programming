#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # la tupla a debe tener como minimo 2 elementos
    if len(tuple_a) < 2:
        if len(tuple_a) == 1:
            tuple_a = (tuple_a[0], 0)
        else:
            tuple_a = (0, 0)
    else:
        tuple_a = tuple_a[:2]
    if len(tuple_b) < 2:
        if len(tuple_b) == 1:
            tuple_b = (tuple_b[0], 0)
        else:
            tuple_b = (0, 0)
    else:
        tuple_b = tuple_b[:2]
    sum_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return sum_tuple
