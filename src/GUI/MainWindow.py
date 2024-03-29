from PySide2.QtWidgets import QMainWindow, QWidget, QPushButton, QMessageBox, QVBoxLayout, QHBoxLayout, QPlainTextEdit, QTabWidget, QFileDialog, QScrollArea, QLabel
from PySide2.QtGui import QIcon, QTextCharFormat, Qt
import sys
sys.path.append("..")
from GUI.Button import Button
from xml_tree.parse_xml import xml2tree
from xml_tree.compression import compress, decompress
from xml_tree.errors_detection import error_detection
from xml_tree.errors_correction import error_correction
from network_graph.User_class import User
from GUI.GraphWindow import GraphWindow

class MainWindow(QMainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle(" XML Analyzer")
        self.setWindowIcon(QIcon("icons/logo.png"))
        self.graphWindow = None
        self.tree = None
        self.stack = []
        self.redo_stack = []
        self.isOpen = False

        self.inputTextArea = QPlainTextEdit()
        self.outputTextArea = QPlainTextEdit()
        self.outputTextArea.setReadOnly(True)
        self.inputTextArea.textChanged.connect(self.closeButtons)

        self.logLayout = QVBoxLayout()
        self.logLayout.addStretch()
        self.logLayout.addWidget(QLabel(""))
        self.logLayout.addStretch()
        # self.logLayout.setContentsMargins(10, 10, 10, 10)
        logWidget = QWidget()
        logWidget.setObjectName("log")
        logWidget.setLayout(self.logLayout)
        self.logTextArea = QScrollArea()
        self.logTextArea.setWidgetResizable(True)
        self.logTextArea.setMaximumHeight(180)
        self.logTextArea.setWidget(logWidget)
        self.logTextArea.verticalScrollBar().rangeChanged.connect(self.scrollHandle)
        
        self.openButton = Button("icons/OpenSymbol", "Open XML")
        self.saveButton = Button("icons/SaveSymbol", "Save\nas XML", 10)
        self.decompressButton = Button("icons/CompressSymbol", "Open Compressed", 10)
        self.compressButton = Button("icons/DeCompressSymbol", "Save as Compressed", 10)
        self.helpButton = Button("icons/HelpSymbol", "Help")
        self.closeButton = Button("icons/CloseSymbol", "Quit")
        
        self.undoButton = Button("icons/UndoSymbol", "Undo")
        self.redoButton = Button("icons/RedoSymbol", "Redo")
        self.showButton = Button("icons/ShowSymbol", "Detect\nErrors", 10)
        self.fixButton = Button("icons/FixSymbol", "Fix Errors")
        self.prettifyButton = Button("icons/FormatSymbol", "Prettify")
        self.minifyButton = Button("icons/MinifySymbol", "Minify")
        self.convertButton = Button("icons/ConvertSymbol", "Convert\nto JSON", 10)
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

        self.openButton.clicked.connect(self.openHandle)
        self.saveButton.clicked.connect(self.saveHandle)
        self.decompressButton.clicked.connect(self.decompressHandle)
        self.compressButton.clicked.connect(self.compressHandle)
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
        self.tabs.addTab(self.buttonBarLayout([self.openButton, self.saveButton, self.decompressButton, self.compressButton, self.helpButton, self.closeButton]), "file")
        self.tabs.addTab(self.buttonBarLayout([self.undoButton, self.redoButton, self.showButton, self.fixButton, self.prettifyButton, self.minifyButton, self.convertButton, self.visualizeButton]), "edit")
        
        body = QHBoxLayout()
        body.addWidget(self.inputTextArea)
        body.addWidget(self.outputTextArea)
        body.setContentsMargins(10,10,10,10)
        
        layout = QVBoxLayout()
        layout.addWidget(self.tabs, 0)
        layout.addLayout(body, 1)
        layout.addWidget(self.logTextArea, 2)
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
            myClassFormat = QTextCharFormat()
            myClassFormat.setForeground(Qt.black)
            self.inputTextArea.setCurrentCharFormat(myClassFormat)
            with open(path[0]) as file_in:
                len = 0
                for line in file_in:
                    if len > 1000:
                        break
                    self.inputTextArea.insertPlainText(line)
                    len += 1
    
    def saveHandle(self):
        path = QFileDialog.getSaveFileName(self, 'Create a file', '', 'xml files (*.xml)')
        if path != ('', ''):
            file = open(path[0], 'w')
            text = self.inputTextArea.toPlainText()
            file.write(text)
            file.close()
            self.sendMessage("File saved successfully!", "green")
        
    def helpHandle(self):
        QMessageBox.about(QPushButton(), "Help", "This is the help Section.")
    
    def closeHandle(self):
        sys.exit()

    def prettifyHandle(self):
        self.outputTextArea.clear()
        self.outputTextArea.insertPlainText(self.tree.prettify())
        self.save_current_state()
        self.sendMessage("Prettifying done successfully!", "green")

    def minifyHandle(self):
        self.outputTextArea.clear()
        self.outputTextArea.insertPlainText(self.tree.minify())
        self.save_current_state()
        self.sendMessage("Minifying done successfully!", "green")

    def convertHandle(self):
        self.outputTextArea.clear()
        self.outputTextArea.insertPlainText(self.tree.convert(False, True))
        self.save_current_state()
        self.sendMessage("Converted to JSON successfully!", "green")

    def showHandle(self):
        text = list(self.inputTextArea.toPlainText().split("\n"))
        errors = error_detection(text)
        if errors is None:
            self.sendMessage("No xml tags found", "#bbbb00")
            pass
        elif errors == []:
            myClassFormat = QTextCharFormat()
            myClassFormat.setForeground(Qt.black)
            self.inputTextArea.setCurrentCharFormat(myClassFormat)
            text = self.inputTextArea.toPlainText()
            self.inputTextArea.clear()
            self.inputTextArea.insertPlainText(text)
            if not self.isOpen:
                self.openButtons()
                self.tree = xml2tree(self.inputTextArea.toPlainText())
            self.sendMessage("No errors in XML", "green")
        else:
            self.sendMessage(f'{len(errors)} error/s found in file:', "red")
            for error in errors:
                if error[1][:11] == "Mismatching":
                    if error[1] == "Mismatching tags":
                        if error[0] == error[2][2]:
                            self.sendMessage(f'in line {error[0]+1}: {error[1]} between {error[2][1]} and {error[2][0]}.', "red")
                        else:
                            self.sendMessage(f'in lines {error[2][2]+1} and {error[0]+1}: {error[1]} between {error[2][1]} and {error[2][0]}.', "red")
                else:
                    self.sendMessage(f'in line {error[0]+1}: {error[1]} for {error[2]}.', "red")
            self.inputTextArea.clear()
            myClassFormat = QTextCharFormat()
            errorLines = []
            for error in errors:
                errorLines.append(error[0])
                if error[1] == "Mismatching tags":
                    errorLines.append(error[2][2])
            for i, line in enumerate(text):
                myClassFormat.setForeground(Qt.black)
                if i in errorLines:
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
        self.inputTextArea.clear()
        myClassFormat = QTextCharFormat()
        myClassFormat.setForeground(Qt.black)
        self.inputTextArea.setCurrentCharFormat(myClassFormat)
        for line in text:
            self.inputTextArea.insertPlainText(line + "\n")
        self.inputTextArea.textCursor().deletePreviousChar()
        if errors == []:
            self.openButtons()
            self.tree = xml2tree(self.inputTextArea.toPlainText())
            self.sendMessage("Errors fixed successfully!", "green")
        else:
            self.sendMessage("ERROR: Can't fix errors. Invalix XML format.", "red")

    def visualizeHandle(self):
        try:
            User.parse_users_node(self.tree)
        except Exception as e:
            self.sendMessage("ERROR: Can't generate network. Invalid social network XML provided.", "red")
        else:
            self.graphWindow = GraphWindow()
            self.graphWindow.show()
            self.graphWindow.showMaximized()
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
            self.sendMessage("File saved successfully!", "green")
    
    def decompressHandle(self):
        path = QFileDialog.getOpenFileName(self, 'Choose a file', '', 'comp files (*.comp)')
        if path != ('', ''):
            text = decompress(path[0])
            self.inputTextArea.clear()
            self.outputTextArea.clear()
            myClassFormat = QTextCharFormat()
            myClassFormat.setForeground(Qt.black)
            self.inputTextArea.setCurrentCharFormat(myClassFormat)
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
        self.isOpen = True
        self.fixButton.disabled = True
        self.prettifyButton.disabled = False
        self.minifyButton.disabled = False
        self.convertButton.disabled = False
        self.visualizeButton.disabled = False
        self.fixButton.setObjectName("disabled")
        self.prettifyButton.setObjectName("enabled")
        self.minifyButton.setObjectName("enabled")
        self.convertButton.setObjectName("enabled")
        self.visualizeButton.setObjectName("enabled")
        self.updateTabs()

    def closeButtons(self):
        self.isOpen = False
        self.fixButton.disabled = True
        self.prettifyButton.disabled = True
        self.minifyButton.disabled = True
        self.convertButton.disabled = True
        self.visualizeButton.disabled = True
        self.fixButton.setObjectName("disabled")
        self.prettifyButton.setObjectName("disabled")
        self.minifyButton.setObjectName("disabled")
        self.convertButton.setObjectName("disabled")
        self.visualizeButton.setObjectName("disabled")
        self.updateTabs()

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

    def closeEvent(self, event):
        if self.graphWindow:
            self.graphWindow.close()