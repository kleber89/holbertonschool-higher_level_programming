#!/usr/bin/bash/python3
"""
    Fish class with methods swim and habitat.
"""


class Fish:
    """
    Fish class with methods swim and habitat.
    """

    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird:
    """
    Bird class with methods fly and habitat.
    """

    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    FlyingFish class that inherits from both Fish and Bird.
    """

    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")
