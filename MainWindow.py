from PySide2.QtWidgets import QMainWindow, QWidget, QPushButton, QMessageBox, QVBoxLayout, QHBoxLayout, QPlainTextEdit, QTabWidget, QFileDialog
from PySide2.QtGui import QIcon, QTextCharFormat, QFont, Qt
import sys
from Button import Button

class MainWindow(QMainWindow):
    
    def __init__(self, tree):
        super(MainWindow, self).__init__()
    
        self.setGeometry(400, 200, 1200, 800)
        self.setWindowTitle(" XML Editor")
        self.setWindowIcon(QIcon("icons/logo.png"))

        inputTextArea = QPlainTextEdit()
        outputTextArea = QPlainTextEdit()
        outputTextArea.setReadOnly(True)

        myClassFormat = QTextCharFormat()
        myClassFormat.setForeground(Qt.red)
        inputTextArea.setCurrentCharFormat(myClassFormat)
        inputTextArea.insertPlainText("This is some red text.")
        
        openButton = Button("icons/OpenSymbol", "Open File")
        saveButton = Button("icons/SaveSymbol", "Save")
        helpButton = Button("icons/HelpSymbol", "Help")
        closeButton = Button("icons/CloseSymbol", "Quit")
        
        fixButton = Button("icons/FixSymbol", "Fix Errors")
        formatButton = Button("icons/FormatSymbol", "Prettify")
        convertButton = Button("icons/ConvertSymbol", "Convert")
        compressButton = Button("icons/CompressSymbol", "Compress")
        
        formatButton.disabled = True
        convertButton.disabled = True
        compressButton.disabled = True
        formatButton.setObjectName("disabled")
        convertButton.setObjectName("disabled")
        compressButton.setObjectName("disabled")

        openButton.clicked.connect(lambda textArea=inputTextArea: self.openHandle(textArea, tree))
        saveButton.clicked.connect(lambda textArea=inputTextArea: self.saveHandle(textArea, tree))
        helpButton.clicked.connect(self.helpHandle)
        closeButton.clicked.connect(self.closeHandle)
        
        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.North)
        tabs.addTab(self.buttonBarLayout([openButton, saveButton, helpButton, closeButton]), "file")
        tabs.addTab(self.buttonBarLayout([fixButton, formatButton, convertButton, compressButton]), "edit")
        
        body = QHBoxLayout()
        body.addWidget(inputTextArea)
        body.addWidget(outputTextArea)
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
        
        
    def openHandle(self, textArea, tree):
        path = QFileDialog.getOpenFileName(self, 'Choose a file', '', 'xml files (*.xml)')
        if path != ('', ''):
            textArea.clear()
            with open(path[0]) as file_in:
                for line in file_in:
                    textArea.insertPlainText(line)
            tree.setTree(path[0])

    def saveHandle(self, textArea, tree):
        path = QFileDialog.getSaveFileName(self, 'Create a file', '', 'xml files (*.xml)')
        if path != ('', ''):
            file = open(path[0], 'w')
            text = textArea.toPlainText()
            file.write(text)
            file.close()
        
    def helpHandle(self):
        QMessageBox.about(QPushButton(), "Help", "This is the help Section.")
    
    def closeHandle(self):
        sys.exit()
    
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