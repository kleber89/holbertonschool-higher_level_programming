#!/usr/bin/env python3
import pickle

class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
       
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except (IOError, pickle.PicklingError) as e:
            print(f"Serialization failed: {e}")

    @classmethod
    def deserialize(cls, filename):
        
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (IOError, pickle.UnpicklingError) as e:
            print(f"Deserialization failed: {e}")
            return None
