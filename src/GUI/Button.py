from PySide2.QtWidgets import QLabel, QPushButton, QVBoxLayout
from PySide2.QtGui import QPixmap
from PySide2.QtCore import Signal, Qt

class Button(QPushButton):

    clicked = Signal()
    hovered = Signal()
    disabled = False
    
    def __init__(self, icon, word, offset = 0):
        super(Button, self).__init__()
        
        self.setMinimumSize(120,140)
        layout = QVBoxLayout(self)
        
        image = QLabel()
        image.setFixedSize(120, 80 - offset)
        pixmap = QPixmap(icon).scaledToWidth(70 - offset)
        image.setPixmap(pixmap)
        image.setAlignment(Qt.AlignCenter)
        
        text = QLabel(word)
        text.setFixedSize(120, 50 + offset)
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
