#!/usr/bin/python3
"""
way to inherit a list
"""


class MyList(list):
    def print_sorted(self):
        """
        Prints the list in ascending order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
