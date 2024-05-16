#!/usr/bin/python3

for i in range(100):
    # Print the number with two digits followed by ", " except for the last number
    print("{:02d}".format(i), end=', ' if i < 99 else '\n')
