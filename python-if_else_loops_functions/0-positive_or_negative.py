#!/usr/bin/python3
import random
number = random.randint(-10, 10)

print(number)
if number > 0:
    print("it is positive")
elif number == 0:
    print("it is zero")
else:
    print("it is negative")
