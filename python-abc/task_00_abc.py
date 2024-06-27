#!/usr/bin/python3
"""
class of Animal
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Animal is an abstract base class that defines
    the blueprint for its subclasses.
    It contains an abstract method sound
    which must be implemented by any non-abstract
    subclass of Animal.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method to be implemented by subclasses.
        Should return the sound made by the animal.
        """
        pass


class Dog(Animal):
    """
    Dog is a subclass of Animal and provides an implementation of the
    abstract method sound. The sound method returns the string "Bark".
    """

    def sound(self):
        """
        Returns the sound made by the dog.
        """
        return "Bark"


class Cat(Animal):
    """
    Cat is a subclass of Animal and provides an implementation of the
    abstract method sound. The sound method returns the string "Meow".
    """

    def sound(self):
        """
        Returns the sound made by the cat.
        """
        return "Meow"
