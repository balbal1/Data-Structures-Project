import sys
sys.path.append("..")
from xml_tree.BinaryTree import BinaryTree

def compress(xmlString):

    # construct the search tree of every character in xml with its frequency
    searchTree = BinaryTree()
    for character in xmlString:
        searchTree.addChild(character)

    # make a list of all character nodes to use in the huffman algorithm
    searchTree = searchTree.leftChild
    treeNodes = searchTree.listNodes()

    # the huffman algorithm: pop the least frequent characters and make them children of single parent
    # whose freqency is the summation of its children freqencies and add the parent to the nodes list
    while len(treeNodes) > 1:
        treeNodes.sort()
        combined = BinaryTree("", treeNodes[0].number + treeNodes[1].number, treeNodes[0], treeNodes[1])
        treeNodes[1] = combined
        treeNodes.pop(0)
    
    # make the encodings of characters using the huffman tree
    huffmanTree = treeNodes[0]
    huffmanTree.encodeCharacters(searchTree, "")
    compressedString = huffmanTree.encodeTree()

    # convert each character in xml to its encoding and store it all in a string
    binaryString = ""
    for character in xmlString:
            binaryString += str(searchTree.getNode(character).encoding)
    
    # split the string into 6-bit chunks
    binaryCharacters = []
    i = 0
    for bit in binaryString:
        if i % 6 == 0:
            binaryCharacters.append(bit)
        else:
            binaryCharacters[i//6] += bit
        i += 1
    binaryCharacters.append(bin(len(binaryCharacters[-1]))[2:])

    # encode the 6-bit chunks to ascii and add it to the compressed string
    compressedString += "_SPLIT_"
    for character in binaryCharacters:
        compressedString += chr(int(character, 2)+62)
    
    return compressedString


def decompress(path):

    # read the compressed string from the file
    file = open(path, "r")
    compressedString = file.read()
    file.close()
    
    # split the tree from the message and construct the huffman tree
    treeString, textString = compressedString.split("_SPLIT_")
    n, huffmanTree = BinaryTree.constructTree(treeString)

    # convert the message to its its ascii encoding and add it all to string
    binaryString = ""
    for character in textString:
        binaryString += (bin(ord(character)-62)[2:]).zfill(6)
    num = -(6+int(binaryString[-6:], 2))
    binaryString = binaryString[:-12] + binaryString[num:-6]

    # reconstruct the xml string using the encoded message and the huffman tree
    xmlString = ""
    currentNode = huffmanTree
    for bit in binaryString:
        if bit == "1":
            currentNode = currentNode.rightChild
        else:
            currentNode = currentNode.leftChild
        if currentNode.rightChild == None and currentNode.leftChild == None:
            xmlString += currentNode.character
            currentNode = huffmanTree

    return xmlString