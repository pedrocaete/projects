from tkinter import *
from ImageManager import ImageManager
from PIL import Image, ImageTk

class ImageViewer:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Image Viewer")
        self.manager = ImageManager()
        self.atualIndex = 0;

        self.imageLabel = Label(root)
        self.imageLabel.grid(row=0, column=0, columnspan=3)

        self.addImagesButton = Button(self.root, text="Adicionar Imagens", command=self.addImages)
        self.addImagesButton.grid(row=1, column=1)

        self.prevButton = Button(self.root, text="<<", command=self.viewPrev)
        self.prevButton.grid(row=1, column=0)

        self.nextButton = Button(self.root, text=">>", command=self.viewNext)
        self.nextButton.grid(row=1, column=2)

        self.status = Label(self.root, text="", bd=1, relief=SUNKEN, anchor=E)
        self.status.grid(row=2, column=0, columnspan=3, sticky= W+E)

        self.loadImages()

    def loadImages(self):
        self.images = self.manager.listImages()
        if self.images:
            self.displayImage()
            self.updateStatusBar()

    def displayImage(self):
        if not self.images:
            return

        path = self.images[self.atualIndex]
        img = Image.open(path)
        img = img.resize((400,400))
        imgTk = ImageTk.PhotoImage(img)
        
        self.imageLabel.config(image=imgTk)

    def addImages(self):
        self.manager.addImages()
        self.loadImages()

    def viewNext(self):
        if self.images and self.atualIndex < len(self.images) - 1:
            self.atualIndex += 1 
        else:
            self.atualIndex = 0
        self.loadImages()

    def viewPrev(self):
        if self.images and self.atualIndex > 0:
            self.atualIndex -= 1 
        else:
            self.atualIndex = len(self.images) - 1
        self.loadImages()

    def updateStatusBar(self):
        self.imageIndex = self.atualIndex + 1
        self.status.config(text="Image " + str(self.imageIndex) + " of " + str(len(self.images)))
