#!/usr/bin/python3
from sys import argv


def add_arguments(args):
    addition = sum(int(argument) for argument in args)
    return addition


if __name__ == "__main__":
    arguments = argv[1:]
    result = add_arguments(arguments)
    print(result)
