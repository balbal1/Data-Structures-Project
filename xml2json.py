
def xml2json(tree, isArray, isRoot=False):
        if isRoot:
            return "{\n" + xml2json(tree,False)[:-2] + "\n}"

        string = "  " * (tree.level + 1)
        if not isArray:
            string += "\"" + tree.name + "\": "
        
        if tree.children == []:
            return string + "\"" + str(tree.text) + "\",\n"
        
        if len(tree.children) > 1 and tree.name[-1] == "s":
            isArray = True
            brackets = ["[", "]"]
        else:
            isArray = False
            brackets = ["{", "}"]

        string += brackets[0] + "\n"
        for child in tree.children:
            string += xml2json(child,isArray)
        return string[:-2] + "\n" + "  " * (tree.level + 1) + brackets[1] + ",\n"
