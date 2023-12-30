from PySide2.QtWidgets import QMainWindow, QWidget, QLabel, QPushButton, QComboBox, QLineEdit, QScrollArea, QVBoxLayout, QHBoxLayout
from PySide2.QtGui import QIcon, QPixmap
from Post import Post
from Post_class import Post as PostClass
from Graph_analysis import Graph_Analysis

class GraphWindow(QMainWindow):
    
    def __init__(self):
        super(GraphWindow, self).__init__()
        
        self.setGeometry(400, 200, 1200, 800)
        self.setWindowTitle(" Graph Viewer")
        self.setWindowIcon(QIcon("icons/logo.png"))
        self.graph = Graph_Analysis()

        self.graph.visualize([])
        graphmap = QPixmap("graph.png")
        self.graphImage = QLabel()
        self.graphImage.setPixmap(graphmap)

        influencerButton = QPushButton("Find most influencer user")
        activeButton = QPushButton("Find most active user")
        mutualButton = QPushButton("Find mutual users")
        suggestButton = QPushButton("Suggest users")
        self.mutualComboButton1 = QComboBox()
        self.mutualComboButton2 = QComboBox()
        self.suggestComboButton = QComboBox()
        names = []
        for user in self.graph.users:
            names.append(f'{user.name} ({user.id})')
        self.mutualComboButton1.addItems(names)
        self.mutualComboButton2.addItems(names[1:])
        self.suggestComboButton.addItems(names)
        self.mutualComboButton1.currentTextChanged.connect(self.updateComboBox)

        influencerButton.setFixedSize(280,40)
        activeButton.setFixedSize(250,40)
        mutualButton.setFixedSize(220,40)
        suggestButton.setFixedSize(220,40)
        self.mutualComboButton1.setFixedHeight(30)
        self.mutualComboButton2.setFixedHeight(30)
        self.suggestComboButton.setFixedHeight(30)

        topButtonsTitle = QLabel("Network Analysis:")
        topButtonsTitle.setObjectName("mainTitle")
        topButtons = QHBoxLayout()
        topButtons.addWidget(influencerButton, 0)
        topButtons.addWidget(activeButton, 1)
        topButtons.setContentsMargins(10,10,10,10)

        mutualButtonsTitle = QLabel("find mutual users between two users:")
        mutualButtonsTitle.setFixedHeight(40)
        mutualButtonsTitle.setObjectName("title")
        mutualButtons = QHBoxLayout()
        mutualButtons.addStretch()
        mutualButtons.addWidget(self.mutualComboButton1, 0)
        mutualButtons.addWidget(self.mutualComboButton2, 1)
        mutualButtons.addStretch()
        mutualButtons.addWidget(mutualButton, 2)
        mutualButtons.setContentsMargins(10,0,10,10)

        suggestButtonsTitle = QLabel("suggest other users to follow for a user:")
        suggestButtonsTitle.setFixedHeight(30)
        suggestButtonsTitle.setObjectName("title")
        suggestButtons = QHBoxLayout()
        suggestButtons.addStretch()
        suggestButtons.addWidget(self.suggestComboButton, 0)
        suggestButtons.addStretch()
        suggestButtons.addWidget(suggestButton, 1)
        suggestButtons.setContentsMargins(10,0,10,20)

        searchTitle = QLabel("Search posts")
        searchTitle.setFixedHeight(30)
        searchTitle.setObjectName("mainTitle")
        self.searchBar = QLineEdit()
        searchButton = QPushButton("Search")
        searchButton.setFixedSize(150,40)

        searchTools = QHBoxLayout()
        searchTools.addWidget(self.searchBar, 0)
        searchTools.addWidget(searchButton, 1)
        
        self.searchResults = QScrollArea()
        
        searchBox = QVBoxLayout()
        searchBox.addLayout(searchTools, 0)
        searchBox.addStretch()
        searchBox.addWidget(self.searchResults, 1)
        searchBox.addStretch()

        upperWidget = QWidget()
        upperWidget.setMaximumWidth(1000)
        upperWidget.setObjectName("toolbar")
        upperBox = QVBoxLayout()
        upperWidget.setLayout(upperBox)
        upperBox.addWidget(topButtonsTitle, 0)
        upperBox.addLayout(topButtons, 1)
        upperBox.addWidget(mutualButtonsTitle, 2)
        upperBox.addLayout(mutualButtons, 3)
        upperBox.addWidget(suggestButtonsTitle, 4)
        upperBox.addLayout(suggestButtons, 5)
        
        lowerWidget = QWidget()
        lowerWidget.setMaximumWidth(1000)
        lowerWidget.setObjectName("toolbar")
        lowerBox = QVBoxLayout()
        lowerWidget.setLayout(lowerBox)
        lowerBox.addWidget(searchTitle, 6)
        lowerBox.addLayout(searchBox, 7)

        self.toolBar = QVBoxLayout()
        self.toolBar.addWidget(upperWidget, 0)
        self.toolBar.addWidget(lowerWidget, 1)

        self.layout = QHBoxLayout()
        self.layout.addLayout(self.toolBar, 0)
        self.layout.addWidget(self.graphImage, 1)
        self.layout.setContentsMargins(10,10,10,10)
        self.layout.addStretch()
        
        influencerButton.clicked.connect(self.influencerHandle)
        activeButton.clicked.connect(self.activeHandle)
        mutualButton.clicked.connect(self.mutualHandle)
        suggestButton.clicked.connect(self.suggestHandle)
        searchButton.clicked.connect(self.searchHandle)

        widget = QWidget()
        widget.setLayout(self.layout)
        widget.setObjectName("body")
        self.setCentralWidget(widget)
    
    def influencerHandle(self):
        self.graph.visualize([self.graph.most_influencer])
        graphmap = QPixmap("graph.png")
        self.graphImage.setPixmap(graphmap)

    def activeHandle(self):
        self.graph.visualize([self.graph.most_active])
        graphmap = QPixmap("graph.png")
        self.graphImage.setPixmap(graphmap)

    def mutualHandle(self):
        id1 = self.mutualComboButton1.currentText()[-2]
        id2 = self.mutualComboButton2.currentText()[-2]
        self.graph.visualize(self.graph.mutual_followers(id1, id2))
        graphmap = QPixmap("graph.png")
        self.graphImage.setPixmap(graphmap)

    def suggestHandle(self):
        id = self.suggestComboButton.currentText()[-2]
        self.graph.visualize(self.graph.suggest_tofollow(id))
        graphmap = QPixmap("graph.png")
        self.graphImage.setPixmap(graphmap)

    def searchHandle(self):
        posts = PostClass.map.get(self.searchBar.text().lower())
        layout = QVBoxLayout()
        if posts:
            for post in posts:
                post = Post(post, "", "")
                layout.addWidget(post)
        widget = QWidget()
        widget.setLayout(layout)
        self.searchResults.setWidget(widget)

    def updateComboBox(self):
        self.mutualComboButton2.clear()
        names = []
        for user in self.graph.users:
            if user.id != self.mutualComboButton1.currentText()[-2]:
                names.append(f'{user.name} ({user.id})')
        self.mutualComboButton2.addItems(names)
