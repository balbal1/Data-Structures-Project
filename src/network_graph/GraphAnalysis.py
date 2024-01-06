import networkx as nx 
import matplotlib.pyplot as plt 
import numpy
import sys
sys.path.append("..")
from network_graph.User_class import User
from network_graph.Post_class import Post

class Graph_Analysis:
    def __init__(self):
        self.users=User.get_all_users()
        self.vertices_no=len(User.get_all_users())
        self.vertices=[]
        self.edges=[]
        self.create_vertices_edges()
        self.most_influencer=self.Most_influencer()
        self.most_active=self.Most_active()

    def create_vertices_edges(self):
        for user in User.get_all_users():
            self.vertices.append(user.name)
            for follow in user.following:
                self.edges.append([user.name.replace(' ', '\n') + "\n" + f'({user.id})',follow.name.replace(' ', '\n') + "\n" + f'({follow.id})']) 

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
    
    def mutual_followers(self, user1id, user2id):
        user1 = User.get_user(user1id)
        user2 = User.get_user(user2id)
        if user1 not in self.users:
            print("Vertex ", user1, " does not exist.")
        elif user2 not in self.users:
            print("Vertex ", user2, " does not exist.")
        followers1=user1.following
        followers2=user2.following
        mutual=[]
        for f in followers1:
            if f in followers2:
                mutual.append(f.name.replace(' ', '\n') + "\n" + f'({f.id})')
        return mutual

    def suggest_tofollow(self, userid):
        user = User.get_user(userid)
        suggest=[]
        for f in user.following:
            for ff in f.following:
                if ff not in user.following and ff is not user and ff not in suggest:
                    suggest.append(ff.name.replace(' ', '\n') + "\n" + f'({ff.id})')
        return suggest

    def search_posts(self, words):
        posts = []
        for word in words:
            new_posts = Post.map.get(word)
            for post in new_posts:
                if post not in posts:
                    posts.append(post)
        return posts

    def visualize(self, v): 
        G = nx.DiGraph()
        G.add_edges_from(self.edges) 
        numpy.random.seed(50)
        plt.figure(1,figsize=(8,8))
        nx.draw_networkx(G, font_size=12, font_color='black', node_size=3000, width=3, arrowsize=20, node_color=['#ff7f50' if (node_name in v)  else '#add8e6' for node_name in list(G.nodes)])
        plt.savefig("icons/graph.png")
        plt.clf()    
