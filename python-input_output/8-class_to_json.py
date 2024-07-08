#!/usr/bin/python3
"""
function that returns the dictionary description with simple
data structure (list, dictionary, string, integer and boolean).
"""


def class_to_json(obj):
    """ Return dic using dict"""
    return obj.__dict__
