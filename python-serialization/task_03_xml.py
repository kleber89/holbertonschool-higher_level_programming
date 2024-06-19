#!/usr/bin/env python3
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):

    # Create the root element
    root = ET.Element("data")

    # Function to add elements recursively
    def add_elements(parent, d):
        for key, value in d.items():
            element = ET.SubElement(parent, key)
            if isinstance(value, dict):
                add_elements(element, value)
            else:
                element.text = str(value)

    # Add elements to the root
    add_elements(root, dictionary)

    # Create the XML tree and write it to the file
    tree = ET.ElementTree(root)
    try:
        tree.write(filename, encoding="utf-8", xml_declaration=True)
        return True
    except Exception as e:
        print(f"An error occurred while writing XML: {e}")
        return False


def deserialize_from_xml(filename):

    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        def parse_element(element):
            children = list(element)
            if children:
                result = {}
                for child in children:
                    result[child.tag] = parse_element(child)
                return result
            else:
                return element.text

        data = {root.tag: parse_element(root)}
        return data["data"]
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return None
    except ET.ParseError as e:
        print(f"An error occurred while parsing XML: {e}")
        return None


# Example usage
if __name__ == "__main__":
    # Example dictionary to serialize
    example_dict = {
        "name": "Alice",
        "age": 30,
        "is_student": False,
        "address": {"street": "123 Main St", "city": "Wonderland"},
    }

    # Serialize the dictionary to XML
    xml_filename = "data.xml"
    if serialize_to_xml(example_dict, xml_filename):
        print("Serialization successful.")

    # Deserialize the XML back to a dictionary
    deserialized_dict = deserialize_from_xml(xml_filename)
    if deserialized_dict is not None:
        print("Deserialization successful.")
        print(deserialized_dict)
    else:
        print("Deserialization failed.")
