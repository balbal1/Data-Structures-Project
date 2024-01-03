from PySide2.QtWidgets import QMainWindow, QWidget, QLabel, QPushButton, QComboBox, QLineEdit, QScrollArea, QVBoxLayout, QHBoxLayout
from PySide2.QtGui import QIcon, QPixmap
import sys
sys.path.append("..")
from GUI.Post import Post
from network_graph.GraphAnalysis import Graph_Analysis

class GraphWindow(QMainWindow):
    
    def __init__(self):
        super(GraphWindow, self).__init__()
        
        self.showMaximized()
        self.setWindowTitle(" Graph Viewer")
        self.setWindowIcon(QIcon("../icons/logo.png"))
        self.graph = Graph_Analysis()

        self.graph.visualize([])
        graphmap = QPixmap("icons/graph.png")
        self.graphImage = QLabel()
        self.graphImage.setPixmap(graphmap)

        self.logLayout = QVBoxLayout()
        self.logLayout.addStretch()
        self.logLayout.addWidget(QLabel(""))
        self.logLayout.addStretch()
        logWidget = QWidget()
        logWidget.setObjectName("log")
        logWidget.setLayout(self.logLayout)
        self.logTextArea = QScrollArea()
        self.logTextArea.setWidgetResizable(True)
        self.logTextArea.setFixedHeight(150)
        self.logTextArea.setWidget(logWidget)
        self.logTextArea.verticalScrollBar().rangeChanged.connect(self.scrollHandle)
        
        outputBox = QVBoxLayout()
        outputBox.addWidget(self.graphImage)
        outputBox.addWidget(self.logTextArea)

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
        self.layout.addLayout(outputBox, 1)
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
        graphmap = QPixmap("icons/graph.png")
        self.graphImage.setPixmap(graphmap)
        self.sendMessage("Most influencer user: " + self.graph.most_influencer.replace("\n", " "), "green")

    def activeHandle(self):
        self.graph.visualize([self.graph.most_active])
        graphmap = QPixmap("icons/graph.png")
        self.graphImage.setPixmap(graphmap)
        self.sendMessage("Most active user: " + self.graph.most_active.replace("\n", " "), "green")

    def mutualHandle(self):
        id1 = self.mutualComboButton1.currentText()[-2]
        id2 = self.mutualComboButton2.currentText()[-2]
        mutual = self.graph.mutual_followers(id1, id2)
        self.graph.visualize(mutual)
        graphmap = QPixmap("icons/graph.png")
        self.graphImage.setPixmap(graphmap)
        if mutual:
            self.sendMessage(f'{len(mutual)} mutual user/s found.', "green")
        else:
            self.sendMessage("Alert: No mutual users.", "#bbbb00")

    def suggestHandle(self):
        id = self.suggestComboButton.currentText()[-2]
        suggest = self.graph.suggest_tofollow(id)
        self.graph.visualize(suggest)
        graphmap = QPixmap("icons/graph.png")
        self.graphImage.setPixmap(graphmap)
        if suggest:
            self.sendMessage(f'{len(suggest)} suggested user/s found.', "green")
        else:
            self.sendMessage("Alert: No suggested users.", "#bbbb00")

    def searchHandle(self):
        words = list(self.searchBar.text().lower().split())
        if not words:
            self.sendMessage("Alert: Search bar is empty", "#bbbb00")
        else:
            posts = self.graph.search_posts(words)
            if not posts:
                self.searchResults.setWidget(QWidget())
                self.sendMessage("No posts found.", "#bbbb00")
            else:
                self.sendMessage(f'{len(posts)} post/s found.', "green")
                layout = QVBoxLayout()
                if posts:
                    for post in posts:
                        post = Post(post.body, post.author, post.topics)
                        layout.addWidget(post)
                widget = QWidget()
                widget.setObjectName("log")
                widget.setLayout(layout)
                self.searchResults.setWidget(widget)

    def updateComboBox(self):
        self.mutualComboButton2.clear()
        names = []
        for user in self.graph.users:
            if user.id != self.mutualComboButton1.currentText()[-2]:
                names.append(f'{user.name} ({user.id})')
        self.mutualComboButton2.addItems(names)

    def sendMessage(self, message, color):
        messageText = QLabel(message)
        messageText.setStyleSheet("font-size: 22px; color: " + color)
        layout = QHBoxLayout()
        layout.addWidget(QLabel("> "))
        layout.addWidget(messageText)
        layout.addStretch()
        layout.addWidget(QWidget())
        layout.addStretch()
        layout.setContentsMargins(0, 0, 0, 0)
        text = QWidget()
        text.setLayout(layout)
        self.logLayout.addWidget(text)

    def scrollHandle(self):
        self.logTextArea.verticalScrollBar().setValue(self.logTextArea.verticalScrollBar().maximum())
