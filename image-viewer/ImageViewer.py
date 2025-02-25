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
        self.imageLabel.pack()

        self.addImagesButton = Button(self.root, text="Adicionar Imagens", command=self.addImages)
        self.addImagesButton.pack()

        self.prevButton = Button(self.root, text="<<", command=self.viewPrev)
        self.prevButton.pack(side="left")

        self.nextButton = Button(self.root, text=">>", command=self.viewNext)
        self.nextButton.pack(side="right")

        self.loadImages()

        imageIndex = self.atualIndex + 1
        self.statusBar = Label(self.root, text="Image " + str(imageIndex) + " of " + str(len(self.images)))
        self.statusBar.pack()

    def loadImages(self):
        self.images = self.manager.listImages()
        if self.images:
            self.displayImage()

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
