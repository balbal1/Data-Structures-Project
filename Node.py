class Node():

    def __init__(self, name = "", text = "", children = [], level = 0):
        self.name = name
        self.text = text
        self.children = children
        self.level = level
    
    def buildTree(self):
        root = Node()
        return root

    def prettify(self):
        string = ""
        for line in self.stringify():
            string += line + "\n"
        return string

    def minify(self):
        if self.children == []:
            return "<" + self.name + ">" + str(self.text) + "</" + self.name + ">"
        string = "<" + self.name + ">"
        for child in self.children:
            string += child.minify()
        string += "</" + self.name + ">"
        return string

    def convert(self, isArray, isRoot = False):
        if isRoot:
            return "{\n" + self.convert(False)[:-2] + "\n}"

        string = "  " * (self.level + 1)
        if not isArray:
            string += "\"" + self.name + "\": "
        
        if self.children == []:
            return string + "\"" + str(self.text) + "\",\n"
        
        if len(self.children) > 1 and self.name[-1] == "s":
            isArray = True
            brackets = ["[", "]"]
        else:
            isArray = False
            brackets = ["{", "}"]

        string += brackets[0] + "\n"
        for child in self.children:
            string += child.convert(isArray)
        return string[:-2] + "\n" + "  " * (self.level + 1) + brackets[1] + ",\n"

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
            id = Node("id", f"{i}", [], 5)
            name = Node("name", names[i], [], 5)
            member.append(Node("member", "", [id, name], 4))
        teamName = Node("name", "Team Penguin", [], 2)
        members = Node("members", "", member, 2)
        team = Node("team", "", [teamName, members], 1)
        self.name = "teams"
        self.children = [team]
        self.level = 0