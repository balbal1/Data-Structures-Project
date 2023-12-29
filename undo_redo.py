self.stack = []
self.redo_stack = []

self.undoButton = Button("icons/UndoSymbol", "Undo")
self.redoButton = Button("icons/RedoSymbol", "Redo")

self.undoButton.clicked.connect(self.undo)
self.redoButton.clicked.connect(self.redo)

self.tabs.addTab(self.buttonBarLayout([self.showButton, self.fixButton, self.prettifyButton, self.minifyButton, self.convertButton,self.undoButton,self.redoButton]), "edit")

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
                
def save_current_state(self):
        current_content = self.outputTextArea.toPlainText()
        if not self.stack or current_content != self.stack[-1]:
            self.stack.append(current_content)

    def undo(self):
        if self.stack:
            current_state = self.stack.pop()
            self.redo_stack.append(current_state)
            self.outputTextArea.clear()
            self.outputTextArea.insertPlainText(self.stack[-1])
        else:
            self.outputTextArea.clear()

    def redo(self):
        if self.redo_stack:
            next_state = self.redo_stack.pop()
            self.outputTextArea.clear()
            self.outputTextArea.insertPlainText(next_state)
        else:
            self.outputTextArea.clear()
