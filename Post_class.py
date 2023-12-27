from Node import Node

class Post:
    all_posts = []

    def __init__(self, body, topics):
        self.body = body
        self.topics = topics
        self.all_posts.append(self)
        
    @classmethod
    def parse_post(cls, node: Node):
        for attrib in node.children:
            if attrib.name == "body":
                body = attrib.text
            elif attrib.name == "topics":
                topics = []
                for topic in attrib.children:
                    topics.append(topic.text)

        return Post(body, topics)
    

