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

    def contains(self, key):
        return key in self.dict

    def is_empty(self):
        return len(self.dict) == 0
    
    @classmethod
    def test(cls):
        map = Map()
        map.put(1, "a")
        map.put(2, "b")
        map.put(3, "c")
        map.put(4, "d")
        map.put(5, "e")
        map.put(6, "f")

        print(map.get(1))
        print(map.get(2))
        print(map.get(3))

        map.delete(1)
        print(map.get(1))
        print(map.get(2))
        

    # Private Methods
    # TODO: Implement the class with red-black tree

