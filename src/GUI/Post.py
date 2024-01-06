from PySide2.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout

class Post(QWidget):
    
    def __init__(self, post, author, topics, words):
        super(Post, self).__init__()
        
        word_list = post.split()
        if len(word_list) > 25:
            post = ""
            for i in range(25):
                post += word_list[i] + " "
            post += "..."

        def highlighting(text):
            POST='<html> '
            listword=text.split()
            for word in listword:
                if word.lower() in words:
                    POST+=f'<span style="background-color:yellow">{word}</span> '
                else:
                    POST+=f'{word} '   
            POST+='</html>'
            return POST
        
        post = highlighting(post)
        postText = QLabel(post)
        postText.setWordWrap(True)
        postText.setContentsMargins(5,5,5,5)
    
        author = highlighting(author)
        postAuthor = QLabel(author)
        postAuthorTitle = QLabel("Author:")

        postTitle = QHBoxLayout()
        postTitle.setContentsMargins(5,5,5,5)
        postTitle.addWidget(postAuthorTitle)
        postTitle.addWidget(postAuthor)
        postTitle.addStretch()
        postTitle.addWidget(QLabel())
        postTitle.addStretch()

        topicsText = ""
        for topic in topics:
            topicsText += topic + ", "
        topicsText = topicsText[:-2]
        topicsText = highlighting(topicsText)
        topicsBar = QLabel("Topics: " + topicsText + ".")

        layout = QVBoxLayout()
        layout.addLayout(postTitle)
        layout.addWidget(postText)
        layout.addWidget(topicsBar)
        
        widget = QWidget()
        widget.setLayout(layout)
        widget.setFixedWidth(600)
        widget.setObjectName("post")
        l = QVBoxLayout()
        l.addWidget(widget)
        l.setContentsMargins(0,0,0,0)

        self.setLayout(l)