from PySide2.QtWidgets import QMainWindow, QWidget, QPushButton, QMessageBox, QVBoxLayout, QHBoxLayout, QPlainTextEdit, QTabWidget, QFileDialog
import sys
from Button import Button

class MainWindow(QMainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()
    
        self.setGeometry(400, 200, 1200, 800)
        
        inputTextArea = QPlainTextEdit()
        outputTextArea = QPlainTextEdit()
                
        openButton = Button("icons/OpenSymbol", "Open File")
        saveButton = Button("icons/SaveSymbol", "Save")
        helpButton = Button("icons/HelpSymbol", "Help")
        closeButton = Button("icons/CloseSymbol", "Quit")
        
        fixButton = Button("icons/FixSymbol", "Fix Errors")
        formatButton = Button("icons/FormatSymbol", "Prettify")
        convertButton = Button("icons/ConvertSymbol", "Convert")
        compressButton = Button("icons/CompressSymbol", "Compress")
        
        openButton.clicked.connect(lambda textArea=inputTextArea: self.openHandle(textArea))
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
        
        
    def openHandle(self, textArea):
        path = QFileDialog.getOpenFileName(self, 'Choose a file', '', 'xml files (*.xml)')
        if path != ('', ''):
            textArea.clear()
            with open(path[0]) as file_in:
                for line in file_in:
                    textArea.insertPlainText(line)
                    
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