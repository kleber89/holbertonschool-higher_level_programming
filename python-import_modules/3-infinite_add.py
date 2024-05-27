#!/usr/bin/python3
import sys

def main():
    argv = sys.argv[1:]  # Exclude the script name
    total = sum(int(arg) for arg in argv)
    print(total)

if __name__ == "__main__":
    main()
