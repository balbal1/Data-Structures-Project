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
            self.stack.append(current_content)

  

    def undo(self):
        if self.stack:
            current_state = self.stack.pop()
            self.redo_stack.append(current_state)
            self.outputTextArea.clear()
            self.outputTextArea.insertPlainText(self.stack[-1] if self.stack else "")
        else:
            self.outputTextArea.clear()
            self.outputTextArea.insertPlainText("")
            # self.redo_stack.append("")

    def redo(self):
        if self.redo_stack:
            next_state = self.redo_stack.pop()
            self.stack.append(next_state)
            self.outputTextArea.clear()
            self.outputTextArea.insertPlainText(next_state)
        else:
            self.outputTextArea.clear()
            self.outputTextArea.insertPlainText("")
            # self.stack.append("")