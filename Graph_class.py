import networkx as nx 
import matplotlib.pyplot as plt 
import numpy

class Graph:
    def __init__(self):
        self.graph=[]
        self.vertices_no=0
        self.vertices=[]
        self.edges=[]

    def add_vertex(self,v):
        if v in self.vertices:
            return f'Vertex{v}already exists'
        else:
            self.vertices_no +=1
            self.vertices.append(v)
            if self.vertices_no > 1:
                for vertex in self.graph:
                    vertex.append(0)
            temp = []
            for i in range(self.vertices_no):
                temp.append(0)
            self.graph.append(temp)


    def add_edge(self,v1, v2):  
        if v1 not in self.vertices:
            return f'Vertex {v1} does not exist'
        elif v2 not in self.vertices:
            return f'Vertex {v2} does not exist'
        else:
            self.edges.append([v1,v2])
            index1 = self.vertices.index(v1)
            index2 = self.vertices.index(v2)
            self.graph[index1][index2] = 1


    def followers(self,v):
        followers=[] 
        if v not in self.vertices:
            print("Vertex ", v, " does not exist.")
        for edge in self.edges:
            if edge[1] == v :
                followers.append(edge[0])
        return followers
    
    def following(self,v):
        following=[] 
        if v not in self.vertices:
            return f'Vertex {v} does not exist'
        for edge in self.edges:
            if edge[0] == v :
                following.append(edge[1])
        return following
    

    def most_influencer(self):
        most=0
        for v in self.vertices:
            if most< len(self.followers(v)):
                most=len(self.followers(v))
                influencer=v          
        return influencer
    
    def most_active(self):
        most=0
        for v in self.vertices:
            if most< len(self.following(v)):
                most=len(self.following(v))
                influencer=v          
        return influencer
    
    def mutual_followers(self,user1,user2):
        if user1 not in self.vertices:
            print("Vertex ", user1, " does not exist.")
        elif user2 not in self.vertices:
            print("Vertex ", user2, " does not exist.")
        followers1=self.followers(user1)
        followers2=self.followers(user2)
        mutual=[]
        for f in followers1:
            if f in followers2:
                mutual.append(f)
        return mutual


    def suggest_tofollow(self,user):
        suggest=[]
        for f in self.followers(user):
            for ff in self.followers(f):
                if ff not in self.followers(user) and ff != user and ff not in suggest:
                    suggest.append(ff)
        return suggest
    
    def suggest_foreach_user(self):
        string=''
        for v in self.vertices:
            string+=f'for {v} suggest {self.suggest_tofollow(v)} \n'
        return string


    def print(self):
        string=''
        for edge in self.edges:
            string+=f'{edge[0]}---> {edge[1]} \n' 
        return string


    def matrix(self):
        return self.graph
    
    def visualize(self, v): 
        G = nx.DiGraph() 
        G.add_edges_from(self.edges) 
        numpy.random.seed(50)
        nx.draw_networkx(G, font_size=22, node_size=1000, width=3, arrowsize=20, node_color=['red' if (node_name in v)  else 'blue' for node_name in list(G.nodes)])
        plt.savefig("graph.png")
        plt.clf()
    

    def makeGraph(self):
        self.add_vertex('1')
        self.add_vertex('2')
        self.add_vertex('3')
        self.add_vertex('4')
        self.add_vertex('5')
        self.add_edge('2','1')
        self.add_edge('3','1')
        self.add_edge('4','2')
        self.add_edge('1','2')
        self.add_edge('3','2')
        self.add_edge('5','3')
        self.add_edge('5','4')
        self.add_edge('1','5')

