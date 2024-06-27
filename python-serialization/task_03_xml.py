import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a dictionary to XML and save to a file.
    """
    root = ET.Element("data")
    add_elements_xml(dictionary, root)
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def add_elements_xml(dictionary, parent):
    """
    function to add dictionary items as child elements to a parent XML element.
    """
    for key, value in dictionary.items():
        if isinstance(value, dict):
            child = ET.Element(key)
            parent.append(child)
            add_elements_xml(value, child)
        else:
            leaf = ET.Element(key)
            leaf.text = str(value)
            parent.append(leaf)


def deserialize_from_xml(filename):
    """
    Deserialize XML data from a file and reconstruct the dictionary.
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    return dict_xml(root)


def dict_xml(element):
    """
    function to reconstruct a dictionary from XML elements.
    """
    dictionary = {}
    for child in element:
        if len(child) == 0:
            dictionary[child.tag] = child.text
        else:
            dictionary[child.tag] = dict_xml(child)
    return dictionary
