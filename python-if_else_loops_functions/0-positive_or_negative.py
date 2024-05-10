#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# YOUR CODE HERE
if number > 0:
    print(number, "it is positive")
elif number == 0:
    print(number, "it is zero")
else:
    print(number, "it is negative")
