from  tkinter import *

class CalculatorButton:
    def __init__(self, root, signal, row, column, entry):
        self.root = root
        self.signal = str(signal)
        self.entry = entry
        self.row = row
        self.column = column
        self.createButton()

    def createButton(self):
        self.button = Button(
            self.root,
            text=str(self.signal),
            padx=30,
            pady=30,
            command=lambda: self.handleClick(),
        )
        self.button.grid(row=self.row, column=self.column, sticky="nsew")

    def handleClick(self):
        if self.signal == "Clear":
            self.entry.delete(0, END)
        elif self.isNegativeNumber():
            self.insertSignal()
        elif not self.operatorFolllowOperator():
            if self.signal == "=":
                self.calculateResult()
            else:
                self.insertSignal()

    def calculateResult(self):
                expression = self.entry.get().replace("x", "*")
                result = eval(expression)
                self.entry.delete(0, END)
                self.entry.insert(0, result)

    def insertSignal(self):
        self.entry.insert(END, self.signal)

    def operatorFolllowOperator(self):
        return self.isLastSignalOperator() and self.isSignalOperator()

    def isLastSignalOperator(self):
        buffer = self.entry.get()
        if(len(buffer) == 0):
            return True
        return buffer[-1] in "+-/x="

    def isSignalOperator(self):
        return self.signal in "+-/x="

    def isNegativeNumber(self):
        if (len(self.entry.get()) == 0 or self.isLastSignalOperator()) and self.signal == "-":
            buffer = self.entry.get()
            if(len(buffer) <2):
                return True
            return not (buffer[-1] == "-" and buffer[-2] == "-")

            

