#!/usr/bin/python3
import sys


def main():
    argv = sys.argv[1:]
    argc = len(argv)

    if argc == 0:
        print("Number of argument(s): 0.")
    else:
        print(
            "Number of argument(s): {} argument{}:".format(
                argc, "" if argc == 1 else "s"
            )
        )
        for i, arg in enumerate(argv, start=1):
            print("{}: {}".format(i, arg))


if __name__ == "__main__":
    main()
