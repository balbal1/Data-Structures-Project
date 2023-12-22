class TreeNode:
    def __init__(self, tag, text=""):
        self.tag = tag
        self.text = text
        self.children = []

def parse_xml(xml_content):

    root = build_tree_from_xml(xml_content)
    return root

def build_tree_from_xml(xml_content):
    stack = []
    current_node = None

    i = 0
    while i < len(xml_content):
        if xml_content[i] == '<':
            if xml_content[i + 1] == '/':
                # Closing tag
                i += 2  # Move past '</'
                end_tag_start = i
                while xml_content[i] != '>':
                    i += 1
                end_tag = xml_content[end_tag_start:i]
                if stack:
                    current_node = stack.pop()
            elif xml_content[i + 1] == '?':
                # XML declaration, skip
                while xml_content[i:i + 2] != '?>':
                    i += 1
                i += 2  # Move past '?>'
            elif xml_content[i + 1] == '!':
                # Skip comments or CDATA
                while xml_content[i:i + 3] != ']]>' and xml_content[i:i + 2] != '--':
                    i += 1
                i += 3 if xml_content[i:i + 3] == ']]>' else 2
            elif xml_content[i + 1] == '/':
                # Closing tag of self-closing tag, skip
                i += 2  # Move past '</'
                while xml_content[i] != '>':
                    i += 1
                i += 1  # Move past '>'
                if stack:
                    current_node = stack.pop()
            else:
                # Opening tag
                i += 1  # Move past '<'
                start_tag_start = i
                while xml_content[i] != '>':
                    i += 1
                start_tag = xml_content[start_tag_start:i]
                node = TreeNode(start_tag)
                if current_node is not None:
                    current_node.children.append(node)
                    stack.append(current_node)
                current_node = node
        else:
            # Text content
            text_start = i
            while i < len(xml_content) and xml_content[i] != '<':
                i += 1
            text = xml_content[text_start:i].strip()
            if text:
                node = TreeNode(text)
                if current_node is not None:
                    current_node.children.append(node)
            i -= 1  # Move back one step to process the opening tag in the next iteration

        i += 1  # Move to the next character
    return current_node

def print_tree(node, indent=0):
    # Print opening tag for the root
    if node.tag:
        print("  " * indent + f"<{node.tag}>{node.text}")

    # Recursively print children
    for child in node.children:
        print_tree(child, indent + 1)

    # Print closing tag for the root if it has children
    if node.children and node.tag:
        print("  " * indent + f"</{node.tag}>")

# Example:
if __name__ == "__main__":
    with open("sample.xml", 'r') as file:
        xml_content = file.read()

    parsed_tree = parse_xml(xml_content)
    print_tree(parsed_tree)
