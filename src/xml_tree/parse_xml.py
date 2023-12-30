import sys
sys.path.append("..")
from xml_tree.Node import Node

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
                    if not is_empty() and tag[1:] == peek().name:
                        pop()
                else:
                    n = Node(tag, level = len(stack))
                    if root is None:
                        root = n
                    else:
                        peek().children.append(n)
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
                peek().text = data
    return root
