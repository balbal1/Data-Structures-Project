import xml.etree.ElementTree as ET

class Node:
    def __init__(self, name="", text="", children=None, level=0):
        self.name = name
        self.text = text
        self.children = children if children is not None else []
        self.level = level

    def minify(self):
        if not self.children:
            return f"<{self.name}>{self.text}</{self.name}>"
        string = f"<{self.name}>"
        for child in self.children:
            string += child.minify()
        string += f"</{self.name}>"
        return string

    def print_tree(self):
        for line in self.stringify():
            print(line)

    def stringify(self):
        if not self.children:
            return ["  " * self.level + f"<{self.name}>{self.text}</{self.name}>"]
        string = [f"  " * self.level + f"<{self.name}>"]
        for child in self.children:
            string.extend(child.stringify())
        string.append(f"  " * self.level + f"</{self.name}>")
        return string

def build_tree_from_xml(xml_element, level=0):
    node = Node()
    node.name = xml_element.tag
    node.text = xml_element.text.strip() if xml_element.text else ""
    node.level = level

    for child_elem in xml_element:
        child_node = build_tree_from_xml(child_elem, level + 1)
        node.children.append(child_node)

    return node

def parse_xml_to_tree(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    return build_tree_from_xml(root)

# Example test:
if __name__ == "__main__":
    file_path = "sample.xml"
    parsed_tree = parse_xml_to_tree(file_path)

    # Print the parsed tree
    parsed_tree.print_tree()
