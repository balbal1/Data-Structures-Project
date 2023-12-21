import networkx as nx 
import matplotlib.pyplot as plt 
from Graph_class import mygraph

class GraphVisualization: 

	def __init__(self): 
		self.visual = [] 
		
	def addEdge(self, edge): 
		self.visual.append(edge) 
		
	def visualize(self): 
		G = nx.DiGraph() 
		G.add_edges_from(self.visual) 
		nx.draw_networkx(G) 
		plt.show() 




G = GraphVisualization() 
for edge in mygraph.edges:
    G.addEdge(edge) 
G.visualize()