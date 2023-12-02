from PySide2.QtWidgets import QLabel, QPushButton, QVBoxLayout
from PySide2.QtGui import QPixmap
from PySide2.QtCore import Signal, Qt

class Button(QPushButton):

    clicked = Signal()
    hovered = Signal()
    
    def __init__(self, icon, word):
        super(Button, self).__init__()
        
        self.setFixedSize(80,100)
        layout = QVBoxLayout()
        
        label = QLabel(self)
        pixmap = QPixmap(icon).scaledToHeight(60)
        label.setPixmap(pixmap)
        label.setAlignment(Qt.AlignCenter)
        
        l = QLabel(word)
        l.setAlignment(Qt.AlignCenter)
        
        layout.addWidget(label)
        layout.addWidget(l)
        layout.setAlignment(Qt.AlignCenter)
        layout.setContentsMargins(0,0,0,0)

        
        self.setLayout(layout)
        
    def mousePressEvent(self,event):
        self.clicked.emit()
    
    def mouseMoveEvent(self,event):
        self.hovered.emit()