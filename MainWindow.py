from PySide2.QtWidgets import QMainWindow, QWidget, QPushButton, QMessageBox, QVBoxLayout, QHBoxLayout, QPlainTextEdit, QTabWidget, QFileDialog
from PySide2.QtGui import QIcon, QTextCharFormat, QFont, Qt
import sys
from Button import Button
from compression import compress, decompress

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
        
        openButton = Button("icons/OpenSymbol", "Open File")
        saveButton = Button("icons/SaveSymbol", "Save")
        helpButton = Button("icons/HelpSymbol", "Help")
        closeButton = Button("icons/CloseSymbol", "Quit")
        
        fixButton = Button("icons/FixSymbol", "Fix Errors")
        formatButton = Button("icons/FormatSymbol", "Prettify")
        convertButton = Button("icons/ConvertSymbol", "Convert")
        compressButton = Button("icons/CompressSymbol", "Save as compressed")
        decompressButton = Button("icons/DecompressSymbol", "Open and decompress")
        
        formatButton.disabled = True
        convertButton.disabled = True
        formatButton.setObjectName("disabled")
        convertButton.setObjectName("disabled")
        openButton.clicked.connect(self.openHandle)
        saveButton.clicked.connect(self.saveHandle)
        helpButton.clicked.connect(self.helpHandle)
        closeButton.clicked.connect(self.closeHandle)
        compressButton.clicked.connect(self.compressHandle)
        decompressButton.clicked.connect(self.decompressHandle)
        
        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.North)
        tabs.addTab(self.buttonBarLayout([openButton, saveButton, helpButton, closeButton]), "file")
        tabs.addTab(self.buttonBarLayout([fixButton, formatButton, convertButton, compressButton, decompressButton]), "edit")
        
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