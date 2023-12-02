
class xmlTree():
    
    def __init__(self, path=""):
        if path != "":
            file = open(path)
            print(file.readlines())
        else:
            print("empty")

    def setTree(self, path):
        file = open(path)
        print(file.readlines())