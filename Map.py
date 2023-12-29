class Node:
    def __init__(self, key, value, color):
        self.key = key
        self.value = value
        self.color = color
        self.left = None
        self.right = None
        self.parent = None


class Map:
    # Public Interface

    def __init__(self):
        self.dict = {}

    def put(self, key, value):
        self.dict[key] = value

    def get(self, key):
        return self.dict[key] if key in self.dict else None

    def delete(self, key):
        del self.dict[key]

   

    def appendlistvalue(self, key, value):
        if self.get(key):
            self.dict[key].append(value)
        else:
            self.dict[key] = [value]



    def contains(self, key):
        return key in self.dict

    def is_empty(self):
        return len(self.dict) == 0
    
    @classmethod
    def test(cls):
        map = Map()
        # map.put(1, "a")
        # map.put(2, "b")
        # map.put(3, "c")
        # map.appendlistvalue(6, "f")
        # map.appendlistvalue(6, "d")

        map.put(4, ["d"])
        map.put(4,map.get(4).append('o'))
        print(map.get(4))
        
Map.test()
    # Private Methods
    # TODO: Implement the class with red-black tree

