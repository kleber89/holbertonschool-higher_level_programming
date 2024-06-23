#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    maxScore = 0
    maxKey = None

    for k in a_dictionary:
        if a_dictionary[k] > maxScore:
            maxScore = a_dictionary[k]
            maxKey = k

    return maxKey
