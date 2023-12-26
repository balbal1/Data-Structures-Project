class Node():

    def __init__(self, name = "", text = "", level = 0):
        self.name = name
        self.text = text
        self.children = []
        self.level = level
    
    def buildTree(self):
        root = Node()
        return root
    
    def prettify(self):
        pass

    def minify(self):
        if self.children == []:
            return "<" + self.name + ">" + str(self.text) + "</" + self.name + ">"
        string = "<" + self.name + ">"
        for child in self.children:
            string += child.minify()
        string += "</" + self.name + ">"
        return string

    def convert(self):
        pass

    def print(self):
        for line in self.stringify():
            print(line)

    def stringify(self):
        if self.children == []:
            return ["  " * self.level + "<" + self.name + ">" + str(self.text) + "</" + self.name + ">"]
        string = ["  " * self.level + "<" + self.name + ">"]
        for child in self.children:
            string.extend(child.stringify())
        string.append("  " * self.level + "</" + self.name + ">")
        return string

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