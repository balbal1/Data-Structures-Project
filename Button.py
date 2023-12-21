from PySide2.QtWidgets import QLabel, QPushButton, QVBoxLayout, QMenu
from PySide2.QtGui import QPixmap, QIcon
from PySide2.QtCore import Signal, Qt, QSize

class Button(QPushButton):

    clicked = Signal()
    hovered = Signal()
    disabled = False
    
    def __init__(self, icon, word):
        super(Button, self).__init__()
        
        self.setMinimumSize(100,120)
        layout = QVBoxLayout(self)
        
        image = QLabel()
        image.setFixedSize(100, 70)
        pixmap = QPixmap(icon).scaledToWidth(70)
        image.setPixmap(pixmap)
        image.setAlignment(Qt.AlignCenter)
        
        text = QLabel(word)
        text.setFixedSize(100, 30)
        text.setWordWrap(True)
        text.setAlignment(Qt.AlignCenter)
        
        layout.addStretch()
        layout.addWidget(image)
        layout.addWidget(text)
        layout.addStretch()
        layout.setContentsMargins(0,0,0,0)
        
        self.setLayout(layout)
        
    def mousePressEvent(self,event):
        if not self.disabled:
            self.clicked.emit()

class DoubleButton(QPushButton):

    clicked = Signal()
    clicked_normal = Signal()
    clicked_compressed = Signal()
    hovered = Signal()
    disabled = False
    
    def __init__(self, icon, word, options):
        super(DoubleButton, self).__init__()
        
        self.setMinimumSize(100, 120)
        layout = QVBoxLayout(self)
        
        self.image = QPushButton()
        self.image.setFixedSize(100, 80)
        self.image.setIcon(QIcon(icon))
        self.image.setIconSize(QSize(70, 70))
        self.image.clicked.connect(self.normal)

        self.text = QPushButton(word)
        menu = QMenu(self)
        self.text.setFixedSize(100, 40)
        menu.addAction(options[0], self.normal)
        menu.addAction(options[1], self.compressed)
        self.text.setMenu(menu)
        
        self.setObjectName("hovered")

        layout.addWidget(self.image)
        layout.addWidget(self.text)
        layout.setContentsMargins(0,0,0,0)

        self.setLayout(layout)
        
    def normal(self):
        self.clicked_normal.emit()

    def compressed(self):
        self.clicked_compressed.emit()

    def mousePressEvent(self,event):
        if not self.disabled:
            self.clicked.emit()
    
    def enterEvent(self, QEvent):
        self.setStyleSheet("border: 2px solid rgb(147, 190, 234)")

    def leaveEvent(self, QEvent):
        self.setStyleSheet("border: 2px solid rgb(245,246,247)")