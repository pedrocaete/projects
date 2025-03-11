import os
import sys
from tkinter import *
import customtkinter as ctk
from calculator_button import CalculatorButton

if getattr(sys, 'frozen', False):
    # Se o programa está rodando como executável
    base_dir = sys._MEIPASS
else:
    # Se o programa está rodando como script
    base_dir = os.path.dirname(os.path.abspath(__file__))

theme_path = os.path.join(base_dir, "theme.json")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme(theme_path)

root = ctk.CTk()
root.title("Calculadora")
entry = ctk.CTkEntry(root, border_width=6)
calculatorButtons = []
signals = ["+", "-", "/", "x"]

for i in range(10):
    calculatorButtons.append(CalculatorButton(root, i, 1+i//3, i%3, entry))

for index, signal in enumerate(signals):
    CalculatorButton(root, signal, 1+index, 3, entry)
    
CalculatorButton(root, "=", 4, 2, entry)
CalculatorButton(root, "Clear", 4, 1, entry)

entry.grid(row=0,column=0, columnspan=4, ipady=20, sticky="nsew")

root.mainloop()
