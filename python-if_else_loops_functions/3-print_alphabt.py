#!/usr/bin/python3

# Loop through ASCII values of lowercase alphabet (97 to 122)
for i in range(97, 123):
    # Check if the character is not 'q' or 'e'
    if chr(i) not in ['q', 'e']:
        # Print each character without newline using string formatting
        print(chr(i), end='')

# abcdfghijklmnoprstuvwxyz
