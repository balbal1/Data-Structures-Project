from PySide2.QtWidgets import QMainWindow, QWidget, QPushButton, QMessageBox, QVBoxLayout, QHBoxLayout, QPlainTextEdit, QTabWidget, QFileDialog
from PySide2.QtGui import QIcon, QTextCharFormat, QFont, Qt
import sys
from Button import Button, DoubleButton
from compression import compress, decompress
from errors_detection import error_detection
from errors_correction import error_correction

class MainWindow(QMainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setGeometry(400, 200, 1200, 800)
        self.setWindowTitle(" XML Editor")
        self.setWindowIcon(QIcon("icons/logo.png"))
        
        self.inputTextArea = QPlainTextEdit()
        self.outputTextArea = QPlainTextEdit()
        self.outputTextArea.setReadOnly(True)

        # How to change font color in inputTextArea
        # myClassFormat = QTextCharFormat()
        # myClassFormat.setForeground(Qt.red)
        # self.inputTextArea.setCurrentCharFormat(myClassFormat)
        # self.inputTextArea.insertPlainText("This is some red text.")                
        
        openButton = DoubleButton("icons/OpenSymbol", "Open", ["Open\r\nXML", "Open\nCompressed"])
        saveButton = DoubleButton("icons/SaveSymbol", "Save", ["Save\nas XML", "Save as\nCompressed"])
        helpButton = Button("icons/HelpSymbol", "Help")
        closeButton = Button("icons/CloseSymbol", "Quit")
        
        showButton = Button("icons/ShowSymbol", "Show Errors")
        fixButton = Button("icons/FixSymbol", "Fix Errors")
        minifyButton = Button("icons/MinifySymbol", "Minify")
        formatButton = Button("icons/FormatSymbol", "Prettify")
        convertButton = Button("icons/ConvertSymbol", "Convert")
        
        minifyButton.disabled = True
        formatButton.disabled = True
        convertButton.disabled = True
        minifyButton.setObjectName("disabled")
        formatButton.setObjectName("disabled")
        convertButton.setObjectName("disabled")
        openButton.clicked_normal.connect(self.openHandle)
        openButton.clicked_compressed.connect(self.decompressHandle)
        saveButton.clicked_normal.connect(self.saveHandle)
        saveButton.clicked_compressed.connect(self.compressHandle)
        helpButton.clicked.connect(self.helpHandle)
        closeButton.clicked.connect(self.closeHandle)
        
        showButton.clicked.connect(self.showHandle)
        fixButton.clicked.connect(self.fixHandle)

        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.North)
        tabs.addTab(self.buttonBarLayout([openButton, saveButton, helpButton, closeButton]), "file")
        tabs.addTab(self.buttonBarLayout([showButton, fixButton, minifyButton, formatButton, convertButton]), "edit")
        
        body = QHBoxLayout()
        body.addWidget(self.inputTextArea)
        body.addWidget(self.outputTextArea)
        body.setContentsMargins(10,10,10,10)
        
        layout = QVBoxLayout()
        layout.addWidget(tabs, 0)
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

    def showHandle(self):
        text = list(self.inputTextArea.toPlainText().split("\n"))
        errors = error_detection(text)
        self.inputTextArea.clear()
        myClassFormat = QTextCharFormat()
        for i, line in enumerate(text):
            myClassFormat.setForeground(Qt.black)
            for error in errors:
                if error[0] == i+1 and error[1] != "Valid":
                    myClassFormat.setForeground(Qt.red)
            self.inputTextArea.setCurrentCharFormat(myClassFormat)
            self.inputTextArea.insertPlainText(line + "\n")

    def fixHandle(self):
        text = list(self.inputTextArea.toPlainText().split("\n"))
        self.inputTextArea.clear()
        text = error_correction(error_detection(text), text)
        for line in text:
            self.inputTextArea.insertPlainText(line + "\n")
    
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