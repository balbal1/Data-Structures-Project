from Node import Node
from Map import Map

class Post:
    all_posts = []
    map=Map()

    def __init__(self, body, topics):
        self.body = body
        self.topics = topics
        self.all_posts.append(self)
        
    @classmethod
    def parse_post(cls, node: Node):
        for attrib in node.children:
            if attrib.name == "body":
                body = attrib.text
                cls.all_posts.append(body)
            
            elif attrib.name == "topics":
                topics = []
                for topic in attrib.children:
                    topics.append(topic.text)

        for word in cls.all_posts[-1].split():
            cls.map.appendlistvalue(word.lower(),cls.all_posts[-1])
        for topic in topics:
            cls.map.appendlistvalue(topic.lower(),cls.all_posts[-1])

        return Post(body, topics)

    @classmethod
    def search(cls, word):
        return cls.map.get(word.lower())