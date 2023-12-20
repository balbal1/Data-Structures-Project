from PySide2.QtWidgets import QApplication
import sys
from MainWindow import MainWindow
from xmlTree import xmlTree
from errors_detection import error_detection
from open_file import open_xml
from Node import myTree
from xml2json import xml2json


tree=xmlTree()
text=open_xml('sample.xml')
error_detection(text)
print(xml2json(myTree,False,True))
app = QApplication(sys.argv)
window = MainWindow(tree)
window.show()

with open("style.qss", "r") as f:
    _style = f.read()
    window.setStyleSheet(_style)

app.exec_()
sys.exit()
