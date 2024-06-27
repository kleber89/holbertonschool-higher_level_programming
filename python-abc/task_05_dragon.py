#!/usr/bin/python3
"""
    Mixin class providing swim functionality.
"""


class SwimMixin:
    """
    Mixin class providing swim functionality.
    """

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """
    Mixin class providing fly functionality.
    """

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Dragon class inheriting from SwimMixin and FlyMixin.
    """

    def roar(self):
        print("The dragon roars!")
