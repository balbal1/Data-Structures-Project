import networkx as nx 
import matplotlib.pyplot as plt 
import numpy
from  User_class import User

class Graph_Analysis:
    def __init__(self):
        self.graph=[]
        self.users=User.get_all_users()
        self.vertices_no=len(User.get_all_users())
        self.vertices=[]
        self.edges=[]
        self.visualEdges=[]
        self.create_vertices_edges()
        self.most_influencer=self.Most_influencer()
        self.most_active=self.Most_active()
    


    def create_vertices_edges(self):
        for user in User.get_all_users():
            self.vertices.append(user.name)
            for follow in user.following:
                self.edges.append([user.name,follow.name])
                self.visualEdges.append([user.name.replace(' ', '\n') + "\n" + f'({user.id})',follow.name.replace(' ', '\n') + "\n" + f'({follow.id})'])
        

    def Most_influencer(self):
        most=0
        for v in User.get_all_users():
            if most< len(v.followers):
                most=len(v.followers)
                influencer=v          
        return influencer.name.replace(' ', '\n') + "\n" + f'({influencer.id})'
    

    def Most_active(self):
        most=0
        for v in User.get_all_users():
            if most< len(v.following):
                most=len(v.following)
                influencer=v          
        return influencer.name.replace(' ', '\n') + "\n" + f'({influencer.id})'
    
    def mutual_followers(self,user1id,user2id):
        user1 = User.get_user(user1id)
        user2 = User.get_user(user2id)
        if user1 not in self.users:
            print("Vertex ", user1, " does not exist.")
        elif user2 not in self.users:
            print("Vertex ", user2, " does not exist.")
        followers1=user1.followers
        followers2=user2.followers
        mutual=[]
        for f in followers1:
            if f in followers2:
                mutual.append(f.name.replace(' ', '\n') + "\n" + f'({f.id})')
        return mutual


    def suggest_tofollow(self,userid):
        user = User.get_user(userid)
        suggest=[]
        for f in user.followers:
            for ff in f.followers:
                if ff not in user.followers and ff is not user and ff not in suggest:
                    suggest.append(ff.name.replace(' ', '\n') + "\n" + f'({ff.id})')
        return suggest
    


    def suggest_foreach_user(self):
        string=''
        for v in self.users:
            string+=f'for {v.name} suggest {self.suggest_tofollow(v)} \n'
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
        G.add_edges_from(self.visualEdges) 
        numpy.random.seed(50)
        plt.figure(1,figsize=(8,8))
        nx.draw_networkx(G, font_size=12, font_color='black', node_size=3000, width=3, arrowsize=20, node_color=['#ff7f50' if (node_name in v)  else '#add8e6' for node_name in list(G.nodes)])
        plt.savefig("graph.png")
        plt.clf()    
