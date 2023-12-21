

class Graph:
    def __init__(self, nodes=[],neighbours=[],edges=[]):
        self.nodes = nodes
        self.neighbours=neighbours
        self.edges=edges

    def generate_edges(self):
        for i in range(len(self.nodes)):
            for neighbour in self.neighbours[i]:
                    self.edges.append([self.nodes[i], neighbour])
        return self.edges


mygraph=Graph(['ali','ahmed'],[['0','omar','hagar','rana','hi, i am ali'],['1','hagar','rana','hi, i am ahmed']])
print(mygraph.generate_edges())