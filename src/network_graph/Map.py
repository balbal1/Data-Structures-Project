
RED = "red"
BLACK = "black"

class Map:
    # Public Interface

    def put(self, key, value, replace=True):
        self.root = self._put(self.root, key, value, replace)

    def get(self, key):        
        node = self.root
        while(node != None):
            if(key < node.key):
                node = node.left
            elif(key > node.key):
                node = node.right
            else:
                return node.value
            
        return []

    def appendlistvalue(self, key, value):
        self.put(key, value, False)


    def contains(self, key):
        return self.get(key) != None

    def is_empty(self):
        return self.root == None
    
        
    # Private Methods
                
    class TNode:
        def __init__(self, key, value, color):
            self.key = key
            self.value = [value]
            self.color = color
            self.left = None
            self.right = None

    
    def __init__(self):
        self.root: Map.TNode = None

    def _is_red(self, node: TNode):
        if node is None:
            return False

        return node.color == RED
    
    def _rotate_left(self, node: TNode) -> TNode:
        h = node
        x = h.right
        h.right = x.left
        x.left = h
        x.color = h.color
        h.color = RED
        return x
    
    def _rotate_right(self, node: TNode) -> TNode:
        h = node
        x = h.left
        h.left = x.right
        x.right = h
        x.color = h.color
        h.color = RED
        return x
    
    def _flip_colors(self, node: TNode):
        node.color = RED
        node.left.color = BLACK
        node.right.color = BLACK

    def _put(self, node: TNode, key, value, replace) -> TNode:
        if node is None:
            return Map.TNode(key, value, RED)
        
        if key < node.key: node.left = self._put(node.left, key, value, replace)
        elif key > node.key: node.right = self._put(node.right, key, value, replace)
        else: 
            if replace: node.value = [value]
            else: node.value.append(value)

        if self._is_red(node.right) and not self._is_red(node.left): node = self._rotate_left(node)
        if self._is_red(node.left) and self._is_red(node.left.left): node = self._rotate_right(node)
        if self._is_red(node.left) and self._is_red(node.right): self._flip_colors(node)

        return node
