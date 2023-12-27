from PySide2.QtWidgets import QMainWindow, QWidget, QLabel, QPushButton, QComboBox, QLineEdit, QMessageBox, QVBoxLayout, QHBoxLayout, QPlainTextEdit, QTabWidget, QFileDialog
from PySide2.QtGui import QIcon, QTextCharFormat, QFont, Qt, QPixmap

class GraphWindow(QMainWindow):
    
    def __init__(self):
        super(GraphWindow, self).__init__()
        
        self.setGeometry(400, 200, 1200, 800)
        self.setWindowTitle(" Graph Viewer")
        self.setWindowIcon(QIcon("icons/logo.png"))
        self.graph = None

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
        
        searchResults = QVBoxLayout()
        
        searchBox = QVBoxLayout()
        searchBox.addLayout(searchTools, 0)
        searchBox.addStretch()
        searchBox.addLayout(searchResults, 1)
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

        layout = QHBoxLayout()
        layout.addLayout(self.toolBar, 0)
        layout.addWidget(self.graphImage, 1)
        layout.setContentsMargins(10,10,10,10)
        layout.addStretch()
        
        widget = QWidget()
        widget.setLayout(layout)
        widget.setObjectName("body")
        self.setCentralWidget(widget)