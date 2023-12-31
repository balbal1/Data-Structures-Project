from PySide2.QtWidgets import QMainWindow, QWidget, QPushButton, QMessageBox, QVBoxLayout, QHBoxLayout, QPlainTextEdit, QTabWidget, QFileDialog
from PySide2.QtGui import QIcon, QTextCharFormat, QFont, Qt
import sys
sys.path.append("..")
from GUI.Button import Button, DoubleButton
from xml_tree.parse_xml import xml2tree
from xml_tree.compression import compress, decompress
from xml_tree.errors_detection import error_detection
from xml_tree.errors_correction import error_correction
from network_graph.User_class import User
from GUI.GraphWindow import GraphWindow

class MainWindow(QMainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setGeometry(400, 200, 1200, 800)
        self.setWindowTitle(" XML Editor")
        self.setWindowIcon(QIcon("../icons/logo.png"))
        self.tree = None
        self.stack = []
        self.redo_stack = []

        self.inputTextArea = QPlainTextEdit()
        self.outputTextArea = QPlainTextEdit()
        self.outputTextArea.setReadOnly(True)
        self.inputTextArea.textChanged.connect(self.closeButtons)           
        
        self.openButton = DoubleButton("icons/OpenSymbol", "Open", ["Open\r\nXML", "Open\nCompressed"])
        self.saveButton = DoubleButton("icons/SaveSymbol", "Save", ["Save\nas XML", "Save as\nCompressed"])
        self.helpButton = Button("icons/HelpSymbol", "Help")
        self.closeButton = Button("icons/CloseSymbol", "Quit")
        
        self.undoButton = Button("icons/UndoSymbol", "Undo")
        self.redoButton = Button("icons/RedoSymbol", "Redo")
        self.showButton = Button("icons/ShowSymbol", "Detect Errors")
        self.fixButton = Button("icons/FixSymbol", "Fix Errors")
        self.prettifyButton = Button("icons/FormatSymbol", "Prettify")
        self.minifyButton = Button("icons/MinifySymbol", "Minify")
        self.convertButton = Button("icons/ConvertSymbol", "Convert")
        self.visualizeButton = Button("icons/VisualizeSymbol", "Visualize Network", 10)
        
        self.undoButton.disabled = True
        self.redoButton.disabled = True
        self.prettifyButton.disabled = True
        self.minifyButton.disabled = True
        self.convertButton.disabled = True
        self.fixButton.disabled = True
        self.undoButton.setObjectName("disabled")
        self.redoButton.setObjectName("disabled")
        self.fixButton.setObjectName("disabled")
        self.prettifyButton.setObjectName("disabled")
        self.minifyButton.setObjectName("disabled")
        self.convertButton.setObjectName("disabled")
        self.visualizeButton.setObjectName("disabled")

        self.openButton.clicked_normal.connect(self.openHandle)
        self.openButton.clicked_compressed.connect(self.decompressHandle)
        self.saveButton.clicked_normal.connect(self.saveHandle)
        self.saveButton.clicked_compressed.connect(self.compressHandle)
        self.helpButton.clicked.connect(self.helpHandle)
        self.closeButton.clicked.connect(self.closeHandle)

        self.showButton.clicked.connect(self.showHandle)
        self.fixButton.clicked.connect(self.fixHandle)
        self.prettifyButton.clicked.connect(self.prettifyHandle)
        self.minifyButton.clicked.connect(self.minifyHandle)
        self.convertButton.clicked.connect(self.convertHandle) 
        self.undoButton.clicked.connect(self.undoHandle)
        self.redoButton.clicked.connect(self.redoHandle)
        self.visualizeButton.clicked.connect(self.visualizeHandle) 

        self.tabs = QTabWidget()
        self.tabs.setTabPosition(QTabWidget.North)
        self.tabs.addTab(self.buttonBarLayout([self.openButton, self.saveButton, self.helpButton, self.closeButton]), "file")
        self.tabs.addTab(self.buttonBarLayout([self.undoButton, self.redoButton, self.showButton, self.fixButton, self.prettifyButton, self.minifyButton, self.convertButton, self.visualizeButton]), "edit")
        
        body = QHBoxLayout()
        body.addWidget(self.inputTextArea)
        body.addWidget(self.outputTextArea)
        body.setContentsMargins(10,10,10,10)
        
        layout = QVBoxLayout()
        layout.addWidget(self.tabs, 0)
        layout.addLayout(body, 1)
        layout.setContentsMargins(0,0,0,0)
        layout.addStretch()
        
        widget = QWidget()
        widget.setLayout(layout)
        widget.setObjectName("body")
        self.setCentralWidget(widget)
        
    def openHandle(self):
        path = QFileDialog.getOpenFileName(self, 'Choose a file', '', 'xml files (*.xml)')
        if path != ('', ''):
            self.inputTextArea.clear()
            self.outputTextArea.clear()
            with open(path[0]) as file_in:
                for line in file_in:
                    self.inputTextArea.insertPlainText(line)
    
    def saveHandle(self):
        path = QFileDialog.getSaveFileName(self, 'Create a file', '', 'xml files (*.xml)')
        if path != ('', ''):
            file = open(path[0], 'w')
            text = self.inputTextArea.toPlainText()
            file.write(text)
            file.close()
        
    def helpHandle(self):
        QMessageBox.about(QPushButton(), "Help", "This is the help Section.")
    
    def closeHandle(self):
        sys.exit()

    def prettifyHandle(self):
        self.outputTextArea.clear()
        self.outputTextArea.insertPlainText(self.tree.prettify())
        self.save_current_state()

    def minifyHandle(self):
        self.outputTextArea.clear()
        self.outputTextArea.insertPlainText(self.tree.minify())
        self.save_current_state()

    def convertHandle(self):
        self.outputTextArea.clear()
        self.outputTextArea.insertPlainText(self.tree.convert(False, True))
        self.save_current_state()

    def showHandle(self):
        text = list(self.inputTextArea.toPlainText().split("\n"))
        errors = error_detection(text)
        if errors is None:
            pass
        elif errors == []:
            self.openButtons()
            self.tree = xml2tree(self.inputTextArea.toPlainText())
            QMessageBox.about(QPushButton(), "Success", "No errors in XML")
        else:
            self.inputTextArea.clear()
            myClassFormat = QTextCharFormat()
            for i, line in enumerate(text):
                myClassFormat.setForeground(Qt.black)
                for error in errors:
                    if error[0] == i and error[1] != "Valid":
                        myClassFormat.setForeground(Qt.red)
                self.inputTextArea.setCurrentCharFormat(myClassFormat)
                self.inputTextArea.insertPlainText(line + "\n")
            self.inputTextArea.textCursor().deletePreviousChar()
            self.fixButton.disabled = False
            self.fixButton.setObjectName("enabled")
            self.updateTabs()

    def fixHandle(self):
        text = list(self.inputTextArea.toPlainText().split("\n"))
        text = error_correction(error_detection(text), text)
        errors = error_detection(text)
        if errors == []:
            self.inputTextArea.clear()
            myClassFormat = QTextCharFormat()
            myClassFormat.setForeground(Qt.black)
            self.inputTextArea.setCurrentCharFormat(myClassFormat)
            for line in text:
                self.inputTextArea.insertPlainText(line + "\n")
            self.inputTextArea.textCursor().deletePreviousChar()
            self.openButtons()
            self.tree = xml2tree(self.inputTextArea.toPlainText())
            QMessageBox.about(QPushButton(), "Success", "Errors fixed successfully!")
        else:
            QMessageBox.about(QPushButton(), "Error", "Invalix XML format. Can't fix errors.")

    def visualizeHandle(self):
        try:
            User.parse_users_node(self.tree)
        except Exception as e:
            QMessageBox.about(QPushButton(), "Error", "Invalid social network XML provided")
        else:
            self.graphWindow = GraphWindow()
            self.graphWindow.show()
            with open("src/styles/graphStyle.qss", "r") as f:
                _style = f.read()
                self.graphWindow.setStyleSheet(_style)

    def compressHandle(self):
        path = QFileDialog.getSaveFileName(self, 'Create a file', '', 'comp files (*.comp)')
        if path != ('', ''):
            file = open(path[0], 'w')
            text = compress(self.inputTextArea.toPlainText())
            file.write(text)
            file.close()
    
    def decompressHandle(self):
        path = QFileDialog.getOpenFileName(self, 'Choose a file', '', 'comp files (*.comp)')
        if path != ('', ''):
            text = decompress(path[0])
            self.inputTextArea.clear()
            self.inputTextArea.insertPlainText(text)
    
    def save_current_state(self):
        current_content = self.outputTextArea.toPlainText()
        if not self.stack or current_content != self.stack[-1]:
            self.stack.append(current_content)
            self.redo_stack = []
            self.undoButton.disabled = False
            self.undoButton.setObjectName("enabled")
            self.redoButton.disabled = True
            self.redoButton.setObjectName("disabled")
            self.updateTabs()

    def undoHandle(self):
        current_state = self.stack.pop()
        self.redo_stack.append(current_state)
        self.outputTextArea.clear()
        self.outputTextArea.insertPlainText(self.stack[-1] if self.stack else "")
        self.redoButton.disabled = False
        self.redoButton.setObjectName("enabled")
        if not self.stack:
            self.undoButton.disabled = True
            self.undoButton.setObjectName("disabled")
        self.updateTabs()

    def redoHandle(self):
        next_state = self.redo_stack.pop()
        self.stack.append(next_state)
        self.outputTextArea.clear()
        self.outputTextArea.insertPlainText(next_state)
        self.undoButton.disabled = False
        self.undoButton.setObjectName("enabled")
        if not self.redo_stack:
            self.redoButton.disabled = True
            self.redoButton.setObjectName("disabled")
        self.updateTabs()


    def openButtons(self):
        self.showButton.disabled = True
        self.fixButton.disabled = True
        self.prettifyButton.disabled = False
        self.minifyButton.disabled = False
        self.convertButton.disabled = False
        self.visualizeButton.disabled = False
        self.showButton.setObjectName("disabled")
        self.fixButton.setObjectName("disabled")
        self.prettifyButton.setObjectName("enabled")
        self.minifyButton.setObjectName("enabled")
        self.convertButton.setObjectName("enabled")
        self.visualizeButton.setObjectName("enabled")
        self.updateTabs()

    def closeButtons(self):
        self.showButton.disabled = False
        self.fixButton.disabled = True
        self.prettifyButton.disabled = True
        self.minifyButton.disabled = True
        self.convertButton.disabled = True
        self.visualizeButton.disabled = True
        self.showButton.setObjectName("enabled")
        self.fixButton.setObjectName("disabled")
        self.prettifyButton.setObjectName("disabled")
        self.minifyButton.setObjectName("disabled")
        self.convertButton.setObjectName("disabled")
        self.visualizeButton.setObjectName("disabled")
        self.updateTabs()

    def updateTabs(self):
        i = self.tabs.currentIndex()
        self.tabs.removeTab(1)
        self.tabs.addTab(self.buttonBarLayout([self.undoButton, self.redoButton, self.showButton, self.fixButton, self.prettifyButton, self.minifyButton, self.convertButton, self.visualizeButton]), "edit")
        if i == 1:
            self.tabs.setCurrentIndex(1)

    def buttonBarLayout(self, buttonArray):
        bar = QHBoxLayout()
        for button in buttonArray:
            bar.addWidget(button)
        bar.addStretch()
        bar.setContentsMargins(10,10,10,0)
        bar.setSpacing(20)
        tab = QWidget()
        tab.setLayout(bar)
        tab.setObjectName("bars")
        return tab