from  tkinter import *
from tkinter import messagebox

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
        try:
            if self.signal == "Clear":
                self.entry.delete(0, END)
            elif self.isNegativeNumber():
                self.insertSignal()
            elif not self.operatorFolllowOperator():
                if self.signal == "=":
                    self.calculateResult()
                else:
                    self.insertSignal()
        except Exception as e:
                messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

    def calculateResult(self):
        try:
                expression = self.entry.get().replace("x", "*")
                result = eval(expression)
                self.entry.delete(0, END)
                self.entry.insert(0, result)
        except SyntaxError:
            messagebox.showerror("Erro de Sintaxe", "Expressão inválida")
        except ZeroDivisionError:
            messagebox.showerror("Erro de Divisão", "Divisão por zero")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao calcular: {e}")

    def insertSignal(self):
        try:
            self.entry.insert(END, self.signal)
        except Exception as e:
            messagebox.showerror("Erro" f"Erro ao inserir sinal: {e}")

    def operatorFolllowOperator(self):
        try:
            return self.isLastSignalOperator() and self.isSignalOperator()
        except Exception as e:
            messagebox.showerror("Erro" f"Erro ao verificar operadores {e}")

    def isLastSignalOperator(self):
        try:
            buffer = self.entry.get()
            if(len(buffer) == 0):
                return True
            return buffer[-1] in "+-/x="
        except Exception as e:
            messagebox.showerror("Erro" f"Erro ao verificar último operador: {e}")

    def isSignalOperator(self):
        try:
            return self.signal in "+-/x="
        except Exception as e:
            messagebox.showerror("Erro" f"Erro ao verificar operador: {e}")

    def isNegativeNumber(self):
        try:
            if (len(self.entry.get()) == 0 or self.isLastSignalOperator()) and self.signal == "-":
                buffer = self.entry.get()
                if(len(buffer) <2):
                    return True
                return not (buffer[-1] == "-" and buffer[-2] == "-")
        except Exception as e:
            messagebox.showerror("Erro" f"Erro ao verificar sinal númerico: {e}")

            

