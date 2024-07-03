#!/usr/bin/python3
"""
class students
"""


class Student:
    """
    Initializes a new Student object.

    Args:
        first_name (str): The student's first name.
        last_name (str): The student's last name.
        age (int): The student's age.
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Helper function to filter attributes based on the provided list.

        Args:
            attrs (list): A list of attribute names to include.

        Returns:
            dict: A dictionary containing the filtered attributes.
        """
        if isinstance(attrs, list):
            return {attrs: getattr(self, attrs) for attrs in attrs
                    if hasattr(self, attrs)}

        return self.__dict__

    def reload_from_json(self, json):
        """
        Updates the object's attributes from a JSON dictionary.
        """
        for key, value in json.items():
            setattr(self, key, value)
