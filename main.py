from PySide2.QtWidgets import QApplication
import sys
from MainWindow import MainWindow
from xmlTree import xmlTree

tree = xmlTree()

app = QApplication(sys.argv)
window = MainWindow()
window.show()

with open("style.qss", "r") as f:
    _style = f.read()
    window.setStyleSheet(_style)

app.exec_()
sys.exit()