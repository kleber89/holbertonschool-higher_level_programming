#!/usr/bin/python3
import sys


def main():

    argv = sys.argv[1:]
    num_arguments = len(argv)

    if num_arguments == 0:
        print("0 arguments.")

    elif num_arguments == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num_arguments))

    for i, arguments in enumerate(argv, 1):
        print("{}: {}".format(i, arguments))


if __name__ == "__main__":
    main()
