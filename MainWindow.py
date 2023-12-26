from PySide2.QtWidgets import QMainWindow, QWidget, QPushButton, QMessageBox, QVBoxLayout, QHBoxLayout, QPlainTextEdit, QTabWidget, QFileDialog
from PySide2.QtGui import QIcon, QTextCharFormat, QFont, Qt
import sys
from Button import Button, DoubleButton
from parse_xml import xml2tree
from compression import compress, decompress
from errors_detection import error_detection
from errors_correction import error_correction

class MainWindow(QMainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setGeometry(400, 200, 1200, 800)
        self.setWindowTitle(" XML Editor")
        self.setWindowIcon(QIcon("icons/logo.png"))
        self.tree = None

        self.inputTextArea = QPlainTextEdit()
        self.outputTextArea = QPlainTextEdit()
        self.outputTextArea.setReadOnly(True)
        self.inputTextArea.textChanged.connect(self.closeButtons)           
        
        self.openButton = DoubleButton("icons/OpenSymbol", "Open", ["Open\r\nXML", "Open\nCompressed"])
        self.saveButton = DoubleButton("icons/SaveSymbol", "Save", ["Save\nas XML", "Save as\nCompressed"])
        self.helpButton = Button("icons/HelpSymbol", "Help")
        self.closeButton = Button("icons/CloseSymbol", "Quit")
        
        self.showButton = Button("icons/ShowSymbol", "Detect Errors")
        self.fixButton = Button("icons/FixSymbol", "Fix Errors")
        self.prettifyButton = Button("icons/FormatSymbol", "Prettify")
        self.minifyButton = Button("icons/MinifySymbol", "Minify")
        self.convertButton = Button("icons/ConvertSymbol", "Convert")
        
        self.prettifyButton.disabled = True
        self.minifyButton.disabled = True
        self.convertButton.disabled = True
        self.fixButton.disabled = True
        self.prettifyButton.setObjectName("disabled")
        self.minifyButton.setObjectName("disabled")
        self.convertButton.setObjectName("disabled")
        self.fixButton.setObjectName("disabled")

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

        self.tabs = QTabWidget()
        self.tabs.setTabPosition(QTabWidget.North)
        self.tabs.addTab(self.buttonBarLayout([self.openButton, self.saveButton, self.helpButton, self.closeButton]), "file")
        self.tabs.addTab(self.buttonBarLayout([self.showButton, self.fixButton, self.prettifyButton, self.minifyButton, self.convertButton]), "edit")
        
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
            with open(path[0]) as file_in:
                for line in file_in:
                    self.inputTextArea.insertPlainText(line)
    
    def saveHandle(self):
        path = QFileDialog.getSaveFileName(self, 'Create a file', '', 'xml files (*.xml)')
        if path != ('', ''):
            file = open(path[0], 'w')
            text = self.textArea.toPlainText()
            file.write(text)
            file.close()
        
    def helpHandle(self):
        QMessageBox.about(QPushButton(), "Help", "This is the help Section.")
    
    def closeHandle(self):
        sys.exit()

    def prettifyHandle(self):
        self.outputTextArea.clear()
        self.outputTextArea.insertPlainText(self.tree.prettify())

    def minifyHandle(self):
        self.outputTextArea.clear()
        self.outputTextArea.insertPlainText(self.tree.minify())

    def convertHandle(self):
        self.outputTextArea.clear()
        self.outputTextArea.insertPlainText(self.tree.convert(False, True))

    def showHandle(self):
        text = list(self.inputTextArea.toPlainText().split("\n"))
        errors = error_detection(text)
        if errors is None:
            pass
        elif errors == []:
            self.openButtons()
            self.tree = xml2tree(self.inputTextArea.toPlainText())
        else:
            self.inputTextArea.clear()
            myClassFormat = QTextCharFormat()
            for i, line in enumerate(text):
                myClassFormat.setForeground(Qt.black)
                for error in errors:
                    if error[0] == i+1 and error[1] != "Valid":
                        myClassFormat.setForeground(Qt.red)
                self.inputTextArea.setCurrentCharFormat(myClassFormat)
                self.inputTextArea.insertPlainText(line + "\n")
            self.inputTextArea.textCursor().deletePreviousChar()
            self.fixButton.disabled = False
            self.fixButton.setObjectName("enabled")
            self.updateTabs()

    def fixHandle(self):
        text = list(self.inputTextArea.toPlainText().split("\n"))
        self.inputTextArea.clear()
        text = error_correction(error_detection(text), text)
        for line in text:
            self.inputTextArea.insertPlainText(line + "\n")
        self.inputTextArea.textCursor().deletePreviousChar()
        self.openButtons()
        self.tree = xml2tree(self.inputTextArea.toPlainText())
    
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
    
    def openButtons(self):
        self.showButton.disabled = True
        self.fixButton.disabled = True
        self.prettifyButton.disabled = False
        self.minifyButton.disabled = False
        self.convertButton.disabled = False
        self.showButton.setObjectName("disabled")
        self.fixButton.setObjectName("disabled")
        self.prettifyButton.setObjectName("enabled")
        self.minifyButton.setObjectName("enabled")
        self.convertButton.setObjectName("enabled")
        self.updateTabs()

    def closeButtons(self):
        self.showButton.disabled = False
        self.fixButton.disabled = True
        self.prettifyButton.disabled = True
        self.minifyButton.disabled = True
        self.convertButton.disabled = True
        self.showButton.setObjectName("enabled")
        self.fixButton.setObjectName("disabled")
        self.prettifyButton.setObjectName("disabled")
        self.minifyButton.setObjectName("disabled")
        self.convertButton.setObjectName("disabled")
        self.updateTabs()

    def updateTabs(self):
        i = self.tabs.currentIndex()
        self.tabs.removeTab(1)
        self.tabs.addTab(self.buttonBarLayout([self.showButton, self.fixButton, self.prettifyButton, self.minifyButton, self.convertButton]), "edit")
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