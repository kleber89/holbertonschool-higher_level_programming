#!/usr/bin/env python3
"""
    class CustomObject
"""
import pickle


class CustomObject:
    """
    class CustomObject
    """

    def __init__(self, name, age, is_student):
        """
        Initializes a new instance of CustomObject.

        Args:
            name (str): The name of the object.
            age (int): The age of the object.
            is_students (bool): The student status of the object.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def serialize(self, filename):
        """
        Serializes the current instance and saves it to a file.

        Args:
            filename (str): The name of the file to save the instance to.

        Returns:
            None: Returns None if an error occurs during serialization.
        """
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except (EOFError, pickle.PickleError) as e:
            print(f"Error serializing object: {e}")
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        load and return an instance of the
        CustomObject from the provided filename

        arg:
            filename
        """
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except (EOFError, pickle.PickleError) as e:
            print(f"Error serializing object: {e}")
            return None

    def display(self):
        """
        Displays the attributes of the object.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is_student: {self.is_student}")
