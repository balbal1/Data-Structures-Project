
from  User_class import User

class Graph_Analysis:
    def __init__(self):
        self.graph=[]
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
                self.edges.append([user.name,follow.name])
        

    def Most_influencer(self):
        most=0
        for v in User.get_all_users():
            if most< len(v.followers):
                most=len(v.followers)
                influencer=v          
        return influencer.name
    

    def Most_active(self):
        most=0
        for v in User.get_all_users():
            if most< len(v.following):
                most=len(v.following)
                influencer=v          
        return influencer.name
    
    def mutual_followers(self,user1,user2):
        if user1 not in self.users:
            print("Vertex ", user1, " does not exist.")
        elif user2 not in self.users:
            print("Vertex ", user2, " does not exist.")
        followers1=user1.followers
        followers2=user2.followers
        mutual=[]
        for f in followers1:
            if f in followers2:
                mutual.append(f.name)
        return mutual


    def suggest_tofollow(self,user):
        suggest=[]
        for f in user.followers:
            for ff in f.followers:
                if ff not in user.followers and ff is not user and ff not in suggest:
                    suggest.append(ff.name)
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
    




User.test()
mygraph=Graph_Analysis()
print(mygraph.most_influencer)
print(mygraph.most_active)
print(mygraph.mutual_followers(User.get_all_users()[2],User.get_all_users()[1]))
print(mygraph.suggest_foreach_user())