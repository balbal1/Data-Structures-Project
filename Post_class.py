from Node import Node
from Map import Map

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
            cls.map.appendlistvalue(word.lower(),cls.all_posts[-1])
        for word in cls.all_posts[-1].body.split():
            cls.map.appendlistvalue(word.lower(),cls.all_posts[-1])
        for topic in post.topics:
            cls.map.appendlistvalue(topic.lower(),cls.all_posts[-1])

        return post

    @classmethod
    def search(cls, word):
        return cls.map.get(word.lower())