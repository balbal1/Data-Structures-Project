from PySide2.QtWidgets import QApplication
import sys
from GUI.MainWindow import MainWindow

app = QApplication(sys.argv)
window = MainWindow()
window.show()

with open("src/styles/mainStyle.qss", "r") as f:
    _style = f.read()
    window.setStyleSheet(_style)

app.exec_()
sys.exit()
