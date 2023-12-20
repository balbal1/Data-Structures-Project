from PySide2.QtWidgets import QLabel, QPushButton, QVBoxLayout
from PySide2.QtGui import QPixmap
from PySide2.QtCore import Signal, Qt

class Button(QPushButton):

    clicked = Signal()
    hovered = Signal()
    disabled = False
    
    def __init__(self, icon, word):
        super(Button, self).__init__()
        
        self.setFixedSize(100,120)
        layout = QVBoxLayout()
        
        label = QLabel(self)
        pixmap = QPixmap(icon).scaledToHeight(60)
        label.setPixmap(pixmap)
        label.setAlignment(Qt.AlignCenter)
        
        l = QLabel(word)
        l.setWordWrap(True)
        l.setAlignment(Qt.AlignCenter)
        
        layout.addWidget(label)
        layout.addWidget(l)
        layout.setAlignment(Qt.AlignCenter)
        layout.setContentsMargins(0,0,0,0)

        
        self.setLayout(layout)
        
    def mousePressEvent(self,event):
        if not self.disabled:
            self.clicked.emit()
    
    def mouseMoveEvent(self,event):
        if not self.disabled:
            self.hovered.emit()