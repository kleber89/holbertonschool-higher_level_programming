#!/usr/bin/python3
"""
way to inherit a list
"""


class MyList(list):
    """
    class my list
    """
    def print_sorted(self):
        """
        Prints a sorted version of the list.
        """
        print(sorted(self))
