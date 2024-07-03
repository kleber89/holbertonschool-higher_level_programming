#!/usr/bin/python3
"""
class students
"""


class Student:
    """
    Defines a student with first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance.

        Returns:
            dict: A dictionary containing all serializable attributes of the student.
        """
        # Initialize an empty dictionary to store the attributes
        obj_dict = {}

        # Iterate over all attributes of the object
        for key in dir(self):
            # Ignore private and special attributes
            if not key.startswith("__") and not callable(getattr(self, key)):
                value = getattr(self, key)
                # Check if the attribute is serializable
                if isinstance(value, (list, dict, str, int, bool)):
                    obj_dict[key] = value

        return obj_dict
