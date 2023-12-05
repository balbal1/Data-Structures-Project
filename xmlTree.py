
class xmlTree():
    
    def __init__(self, path=""):
        if path != "":
            file = open(path)
            file.readlines()
        else:
            print("empty")

    def setTree(self, path):
        file = open(path)
        file.readlines()

