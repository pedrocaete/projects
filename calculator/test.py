from tkinter import *
from PIL import ImageTk, Image

root = Tk()

img = ImageTk.PhotoImage(Image.open("/home/pedro/Downloads/side-shot-code-editor-using-react-js.jpg"))
label = Label(root, image=img)
label.pack()

root.mainloop()
