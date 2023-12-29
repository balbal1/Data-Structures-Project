import networkx as nx 
import matplotlib.pyplot as plt 
from Graph_analysis import mygraph

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




g = GraphVisualization() 
for edge in mygraph.edges:
    g.addEdge(edge) 
g.visualize()
