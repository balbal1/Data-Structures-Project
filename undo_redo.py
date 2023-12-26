class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return f"Node({self.data})"

class Stack:
    def __init__(self):
        self.pointer = None

    def push(self, x):
        if not isinstance(x, Node):
            x = Node(x)

        if self.is_empty():
            self.pointer = x
        else:
            x.next = self.pointer
            self.pointer.prev = x
            self.pointer = x

    def pop(self):
        if self.is_empty():
            print(f'Stack Underflow')
        else:
            self.pointer = self.pointer.next

    def is_empty(self):
        return self.pointer is None

    def __str__(self):
        string = ''
        current = self.pointer
        while current:
            string += f'{current.data}->'
            current = current.next
        if string:
            print(f'Stack Pointer = {self.pointer.data}')
            return f'[{string[:-2]}]'
        return '[]'

    def undo(self):
        x = self.pointer
        self.pop()
        print(x)

    def redo(self):
        x = self.pointer.prev
        if x is None:
            print("nothing to redo")
        else:
            self.push(x)
            print(x)

if __name__ == "__main__":
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)

    print("stack is:")
    print(stack)
    print()

    stack.undo()

    print("after undo:")
    print(stack)
    print()

    stack.redo()

    print("after redo:")
    print(stack)
