#!/usr/bin/python3

for i in range(10):
    # Loop through the second digit from the first digit + 1 to 9
    for j in range(i + 1, 10):
        # Print the combination of two digits with two digits each
        print("{:d}{:d}".format(i, j), end=', ' if i < 9 or j < 9 else '\n')
