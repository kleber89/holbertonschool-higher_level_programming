import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary into XML format and save it to a file.

    Args:
    - dictionary (dict): Python dictionary to be serialized.
    - filename (str): Filename to save the XML data.

    Returns:
    - None
    """
    root = ET.Element("data")
    for key, value in dictionary.items():
        element = ET.SubElement(root, key)
        element.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """
    Deserialize XML data from a file into a Python dictionary.

    Args:
    - filename (str): Filename of the XML file to deserialize.

    Returns:
    - dict: Python dictionary containing deserialized data.
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    result = {}
    for child in root:
        result[child.tag] = convert_value(child.text)

    return result


def convert_value(value):
    """
    Helper function to convert string values from XML to appropriate Python types.

    Args:
    - value (str): String value to convert.

    Returns:
    - Converted value (int, float, str, etc.)
    """
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            return value
