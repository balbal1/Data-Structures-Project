from Node import Node
from Post_class import Post
from Map import Map
from parse_xml import xml2tree

class User:
    _all_users = []
    _users_map = Map()

    @classmethod
    def get_user(cls, id):
        return cls._users_map.get(id)[0]
    
    @classmethod
    def get_all_users(cls):
        return cls._all_users

    @classmethod
    def parse_users_node(cls, node: Node):
        # TODO: Parse users from node class
        
        if node.name == "users":
            for user in node.children:
                posts = []
                followers_ids = []
                for attrib in user.children:
                    if attrib.name == "id":
                        id = attrib.text
                    elif attrib.name == "name":
                        name = attrib.text
                    elif attrib.name == "posts":
                        for post in attrib.children:
                            posts.append(Post.parse_post(post))
                    elif attrib.name == "followers":
                        for follower in attrib.children:
                            followers_ids.append(follower.children[0].text)
                            
                cls(id, name, posts, followers_ids)
        else:
            raise ValueError("Invalid XML node provided; expected 'users' node")
         

        cls._populate_followers()
        cls._populate_following()

    def __init__(self, id, name, posts, followers_ids):
        self.id = id
        self.name = name
        self.posts = posts
        self.followers_ids = followers_ids
        self.followers = []
        self.following = []

        self._all_users.append(self)
        self._users_map.put(self.id, self)

    
    @classmethod
    def _populate_followers(cls):
        for user in cls._all_users:
            for follower_id in user.followers_ids:
                follower = cls.get_user(follower_id)
                follower.followers.append(user)
    
    @classmethod
    def _populate_following(cls):
        for user in cls._all_users:
            for follower in user.followers:
                follower.following.append(user)

    @classmethod
    def print_all_users(cls):
        for user in User.get_all_users():
            print("User: " + user.name)
            print("ID: " + user.id)
            print("Followers: ", end="")
            for follower in user.followers:
                print(follower.name, end=" - ")

            print("\nFollowing: ", end="")
            for following in user.following:
                print(following.name, end=" - ")

            print("\n\nPosts:")
            for post in user.posts:
                print(post.body, end=" - ")
                print(post.topics)

            print(Post.map.get('sports'))

            print("------")

    @classmethod
    def test(cls):
        with open('./sample.xml', 'r') as file:
            data = file.read()

        node = xml2tree(data)

        # node.print()

        User.parse_users_node(node)

        User.print_all_users()

User.test()