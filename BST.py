class BinaryTree():

    def __init__(self, character = "", number = 1, rightChild = None, leftChild = None):
        self.character = character
        self.number = number
        self.encoding = ""
        self.rightChild = rightChild
        self.leftChild = leftChild

    def addChild(self, character):
        if (self.character == character):
            self.number += 1
        elif (self.character > character):
            if self.rightChild != None:
                self.rightChild.addChild(character)
            else:
                self.rightChild = BinaryTree(character)
        else:
            if self.leftChild != None:
                self.leftChild.addChild(character)
            else:
                self.leftChild = BinaryTree(character)
    
    def getNode(self, character):
        if (self.character == character):
            return self
        elif (self.character > character):
            if self.rightChild != None:
                return self.rightChild.getNode(character)
        else:
            if self.leftChild != None:
                return self.leftChild.getNode(character)

    def listNodes(self):
        nodesList = []
        if self.rightChild != None:
            nodesList.extend(self.rightChild.listNodes())
        if self.leftChild != None:
            nodesList.extend(self.leftChild.listNodes())
        nodesList.append(BinaryTree(self.character, self.number))
        return nodesList
    
    def encodeCharacters(self, tree, encoding):
        if self.character != "":
            node = tree.getNode(self.character)
            node.encoding = encoding
        if self.rightChild != None:
            self.rightChild.encodeCharacters(tree, encoding + "1")
        if self.leftChild != None:
            self.leftChild.encodeCharacters(tree, encoding + "0")

    def encodeTree(self):
        if self.rightChild == None and self.rightChild == None:
            return "1" + self.character
        rightString = ""
        leftString = ""
        if self.rightChild != None:
            rightString = self.rightChild.encodeTree()
        if self.leftChild != None:
            leftString = self.leftChild.encodeTree()
        return "0" + rightString + leftString

    def constructTree(s):
        if s[0] == '1':
            return 2, BinaryTree(s[1])
        combined = BinaryTree()
        n1, rightChild = BinaryTree.constructTree(s[1:])
        n2, leftChild = BinaryTree.constructTree(s[n1+1:])
        combined.rightChild = rightChild
        combined.leftChild = leftChild
        return n1 + n2 + 1, combined

    def __lt__(self, other):
         return self.number < other.number

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        
        # No child.
        if self.rightChild is None and self.leftChild is None:
            line = '%s' % self.character
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.rightChild is None:
            lines, n, p, x = self.leftChild._display_aux()
            s = '%s' % self.character
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.leftChild is None:
            lines, n, p, x = self.rightChild._display_aux()
            s = '%s' % self.character
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        leftChild, n, p, x = self.leftChild._display_aux()
        rightChild, m, q, y = self.rightChild._display_aux()
        s = '%s' % self.character
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            leftChild += [n * ' '] * (q - p)
        elif q < p:
            rightChild += [m * ' '] * (p - q)
        zipped_lines = zip(leftChild, rightChild)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2
        