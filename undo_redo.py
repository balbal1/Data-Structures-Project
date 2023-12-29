def save_current_state(self):
            current_content = self.outputTextArea.toPlainText()
            self.stack.append(current_content)

    def undo(self):
        if len(self.stack) > 1:
            last_operation = self.stack.pop()
            previous_state = self.stack[-1]
            self.outputTextArea.clear()
            self.outputTextArea.insertPlainText(previous_state)
            self.redo_stack.append(self.stack.pop())
        else:
            self.outputTextArea.clear()
            self.outputTextArea.insertPlainText("")
            self.redo_stack.append("")


    def redo(self):
        if self.redo_stack:
            self.outputTextArea.clear()
            self.outputTextArea.insertPlainText(self.redo_stack.pop())
            self.stack.append(self.redo_stack.pop())
        else:
            self.outputTextArea.clear()
            self.outputTextArea.insertPlainText("")
            self.stack.append(self.redo_stack.pop())
