class Graph:
    def __init__(self):
        self.graph=[]
        self.vertices_no=0
        self.vertices=[]
        self.edges=[]

    def add_vertex(self,v):
        if v in self.vertices:
            print('Vertex',v,'already exists')
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
            print("Vertex ", v1, " does not exist.")
        elif v2 not in self.vertices:
            print("Vertex ", v2, " does not exist.")
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
            print("Vertex ", v, " does not exist.")
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


    def print(self):
        for edge in self.edges:
            print(edge[0],'--->',edge[1])   


    def matrix(self):
        return self.graph
    


mygraph=Graph()
mygraph.add_vertex('1')
mygraph.add_vertex('2')
mygraph.add_vertex('3')
mygraph.add_vertex('4')
mygraph.add_edge('1','2')
mygraph.add_edge('1','3')
mygraph.add_edge('4','2')
mygraph.add_edge('4','3')
mygraph.print()
print(mygraph.mutual_followers('2','3'))

