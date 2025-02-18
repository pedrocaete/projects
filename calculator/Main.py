from tkinter import *
from CalculatorButton import CalculatorButton

root = Tk()
entry = Entry(root, width=50)
calculatorButtons = []
signals = ["+", "-", "/", "x"]

for i in range(10):
    calculatorButtons.append(CalculatorButton(root, i, 1+i//3, i%3, entry))

for index, signal in enumerate(signals):
    CalculatorButton(root, signal, 1+index, 3, entry)
    
CalculatorButton(root, "=", 4, 2, entry)
CalculatorButton(root, "Clear", 4, 1, entry)

entry.grid(row=0,column=0, columnspan=4, ipady=20)

root.mainloop()
