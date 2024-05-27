#!/usr/bin/python3
import sys

def main():
    argv = sys.argv[1:]  # Exclude the script name
    num_args = len(argv)

    if num_args == 0:
        print("Number of argument(s):.")
    elif num_args == 1:
        print(f"Number of argument(s): {num_args} argument:")
    else:
        print(f"Number of argument(s): {num_args} arguments:")

    for i, arg in enumerate(argv, start=1):
        print(f"{i}: {arg}")

if __name__ == "__main__":
    main()
