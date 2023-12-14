class Node():

    name = ""
    text = ""
    children = []
    level = 0

    def __init__(self, name = "", text = "", children = [], level = 0):
        self.name = name
        self.text = text
        self.children = children
        self.level = level
    
    def buildTree(self):
        root = Node()
        return root
    
    def prettify(self):
        pass

    def minify(self):
        pass

    def convert(self):
        pass

    def compress(self):
        pass

    def decompress(self):
        pass

    def print(self):
        print("  " * self.level, "<" + self.name + ">", self.text)
        for i in self.children:
            i.print()

    def getTest(self):
        names = ["Ali", "Ahmed", "Ahmed", "Hagar", "Rana"]
        member = []
        for i in range(5):
            id = Node("id", i, [], 5)
            name = Node("name", names[i], [], 5)
            member.append(Node("member", "", [id, name], 4))
        teamName = Node("name", "Team Penguin", [], 2)
        members = Node("members", "", member, 2)
        team = Node("team", "", [teamName, members], 1)
        self.name = "teams"
        self.children = [team]
        self.level = 0


myTree = Node()
myTree.getTest()
myTree.print()