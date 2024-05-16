#!/usr/bin/python3


def print_last_digit(number):
   
    number = abs(number)

    
    last_digit = number % 10

    
    print(last_digit)

    
    return last_digit

# Test the function
print_last_digit(12345)  # Output: 5
