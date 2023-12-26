class Node:
    def __init__(self, name: str, tag_open: bool = False):
        self.name = name
        self.tag_open = tag_open
        self.child = []

def xml2tree(s: str) -> Node:
    stack = []

    def is_empty() -> bool:
        return len(stack) == 0

    def push(n: Node):
        stack.append(n)

    def pop():
        stack.pop()

    def peek() -> Node:
        return stack[-1]

    root = None
    i = 0
    while i < len(s):
        if s[i] == '<':
            start = i
            i += 1
            while i < len(s) and s[i] != '>':
                i += 1
            if i < len(s) and s[i] == '>':
                tag = s[start + 1:i]
                if tag.startswith('/'):
                    if not is_empty() and peek().tag_open and tag[1:] == peek().name:
                        pop()
                else:
                    n = Node(tag, tag_open=True)
                    if root is None:
                        root = n
                    else:
                        peek().child.append(n)
                    push(n)
                i += 1
            else:
                raise ValueError("Invalid XML syntax")
        else:
            start = i
            while i < len(s) and s[i] != '<':
                i += 1
            data = s[start:i].strip()
            if data:
                n = Node(data)
                peek().child.append(n)
    return root

def print_tree(r: Node, level: int = 0) -> None:
    def tab():
        for i in range(level):
            print("  ", end="")

    level += 1
    tab()
    print(f"{r.name}({level})")
    for child in r.child:
        print_tree(child, level)
    level -= 1

# Example:
if __name__ == "__main__":
    with open("sample.xml", 'r') as file:
        xml_content = file.read()

    parsed_tree = xml2tree(xml_content)
    print_tree(parsed_tree)
