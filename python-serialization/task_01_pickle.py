import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the attributes of the object.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the object instance and save it to a file using pickle.

        Args:
        - filename (str): Filename to save the serialized object.

        Returns:
        - None
        """
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
            print(f"Serialized object saved to {filename}")
        except IOError as e:
            print(f"Error: {e}")
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object instance from a file using pickle.

        Args:
        - filename (str): Filename to load the serialized object from.

        Returns:
        - CustomObject instance: Deserialized CustomObject instance.
          Returns None if file not found or other exceptions occur.
        """
        try:
            with open(filename, "rb") as file:
                obj = pickle.load(file)
            if isinstance(obj, cls):
                print(f"Deserialized object loaded from {filename}")
                return obj
            else:
                print(
                    f"Error: File {filename} does not contain an instance of CustomObject"
                )
                return None
        except (IOError, pickle.PickleError) as e:
            print(f"Error: {e}")
            return None
