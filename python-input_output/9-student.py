#!/usr/bin/python3
"""
This is a module for defining a Student class.
"""


class Student:
    """A class representing a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize the student with first name, last name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Return dict for students """
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
