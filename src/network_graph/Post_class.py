import sys
sys.path.append("..")
from xml_tree.Node import Node
from network_graph.Map import Map

class Post:
    all_posts = []
    map=Map()

    def __init__(self, author, body, topics):
        self.author = author
        self.body = body
        self.topics = topics
        self.all_posts.append(self)
        
    @classmethod
    def parse_post(cls, node: Node, author):
        post = Post(author, "", [])
        for attrib in node.children:
            if attrib.name == "body":
                post.body = attrib.text
            
            elif attrib.name == "topics":
                for topic in attrib.children:
                    post.topics.append(topic.text)

        cls.all_posts.append(post)
        for word in author.split():
            cls.map.appendlistvalue(word.lower(),post)
        for word in post.body.split():
            if post not in cls.map.get(word.lower()):
                cls.map.appendlistvalue(word.lower(),post)
        for topic in post.topics:
            cls.map.appendlistvalue(topic.lower(),post)

        return post

    @classmethod
    def search(cls, word):
        return cls.map.get(word.lower())