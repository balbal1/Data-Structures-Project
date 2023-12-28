from PySide2.QtWidgets import QMainWindow, QWidget, QLabel, QPushButton, QComboBox, QLineEdit, QScrollArea, QVBoxLayout, QHBoxLayout
from PySide2.QtGui import QIcon, QPixmap
from Post import Post
from Graph_class import Graph

class GraphWindow(QMainWindow):
    
    def __init__(self):
        super(GraphWindow, self).__init__()
        
        self.setGeometry(400, 200, 1200, 800)
        self.setWindowTitle(" Graph Viewer")
        self.setWindowIcon(QIcon("icons/logo.png"))
        self.graph = Graph()

        self.graph.makeGraph()
        self.graph.visualize([])
        graphmap = QPixmap("graph.png")
        self.graphImage = QLabel()
        self.graphImage.setPixmap(graphmap)

        influencerButton = QPushButton("Find most influencer user")
        activeButton = QPushButton("Find most active user")
        mutualButton = QPushButton("Find mutual users")
        suggestButton = QPushButton("Suggest users")
        mutualComboButton1 = QComboBox()
        mutualComboButton2 = QComboBox()
        suggestComboButton = QComboBox()
        mutualComboButton1.addItems(["Ahmed Ali (1)", "Yasser Ahmed (2)", "Mohamed Sherif (3)"])
        mutualComboButton2.addItems(["Ahmed Ali (1)", "Yasser Ahmed (2)", "Mohamed Sherif (3)"])
        suggestComboButton.addItems(["Ahmed Ali (1)", "Yasser Ahmed (2)", "Mohamed Sherif (3)"])

        influencerButton.setFixedSize(280,40)
        activeButton.setFixedSize(250,40)
        mutualButton.setFixedSize(220,40)
        suggestButton.setFixedSize(220,40)
        mutualComboButton1.setFixedHeight(30)
        mutualComboButton2.setFixedHeight(30)
        suggestComboButton.setFixedHeight(30)

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
        mutualButtons.addWidget(mutualComboButton1, 0)
        mutualButtons.addWidget(mutualComboButton2, 1)
        mutualButtons.addStretch()
        mutualButtons.addWidget(mutualButton, 2)
        mutualButtons.setContentsMargins(10,0,10,10)

        suggestButtonsTitle = QLabel("suggest other users to follow for a user:")
        suggestButtonsTitle.setFixedHeight(30)
        suggestButtonsTitle.setObjectName("title")
        suggestButtons = QHBoxLayout()
        suggestButtons.addStretch()
        suggestButtons.addWidget(suggestComboButton, 0)
        suggestButtons.addStretch()
        suggestButtons.addWidget(suggestButton, 1)
        suggestButtons.setContentsMargins(10,0,10,20)

        searchTitle = QLabel("Search posts")
        searchTitle.setFixedHeight(30)
        searchTitle.setObjectName("mainTitle")
        searchBar = QLineEdit()
        searchButton = QPushButton("Search")
        searchButton.setFixedSize(150,40)

        searchTools = QHBoxLayout()
        searchTools.addWidget(searchBar, 0)
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
        self.graph.visualize(['5'])
        graphmap = QPixmap("graph.png")
        self.graphImage.setPixmap(graphmap)

    def activeHandle(self):
        self.graph.visualize(['3'])
        graphmap = QPixmap("graph.png")
        self.graphImage.setPixmap(graphmap)

    def mutualHandle(self):
        self.graph.visualize(['2', '4'])
        graphmap = QPixmap("graph.png")
        self.graphImage.setPixmap(graphmap)

    def suggestHandle(self):
        self.graph.visualize(['1', '3', '4'])
        graphmap = QPixmap("graph.png")
        self.graphImage.setPixmap(graphmap)

    def searchHandle(self):
        posts = [["Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.", "Ahmed Ali", ["economy", "finance"]],
                 ["Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.", "Ahmed Ali", ["solar_energy"]],
                 ["Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.", "Yasser Ahmed", ["education"]],
                 ["Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.", "Mohamed Sherif", ["sports"]]]
        layout = QVBoxLayout()
        for post in posts:
            post = Post(post[0], post[1], post[2])
            layout.addWidget(post)
        widget = QWidget()
        widget.setLayout(layout)
        self.searchResults.setWidget(widget)