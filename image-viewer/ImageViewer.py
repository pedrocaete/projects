from tkinter import *
from ImageManager import ImageManager
from PIL import Image, ImageTk

class ImageViewer:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Image Viewer")
        self.manager = ImageManager()
        self.atualIndex = 0
        self.images = []

        # Inicializa a interface
        self.create_widgets()
        self.load_images()

    def create_widgets(self):
        self.create_image_label()
        self.create_buttons()
        self.create_status_bar()

    def create_image_label(self):
        self.imageLabel = Label(self.root)
        self.imageLabel.grid(row=0, column=0, columnspan=3)

    def create_buttons(self):
        self.addImagesButton = Button(self.root, text="Adicionar Imagens", command=self.add_images)
        self.addImagesButton.grid(row=1, column=1)

        self.prevButton = Button(self.root, text="<<", command=self.view_prev)
        self.prevButton.grid(row=1, column=0)

        self.nextButton = Button(self.root, text=">>", command=self.view_next)
        self.nextButton.grid(row=1, column=2)

    def create_status_bar(self):
        """Cria a barra de status."""
        self.status = Label(self.root, text="", bd=1, relief=SUNKEN, anchor=E)
        self.status.grid(row=2, column=0, columnspan=3, sticky=W+E)

    def update_status_bar(self):
        self.imageIndex = self.atualIndex + 1
        self.status.config(text="Image " + str(self.imageIndex) + " of " + str(len(self.images)))

    def load_images(self):
        self.images = self.manager.list_images()
        if self.images:
            self.display_image()
            self.update_status_bar()

    def display_image(self):
        if not self.images:
            return

        path = self.images[self.atualIndex]
        img = Image.open(path)
        img = img.resize((400,400))
        imgTk = ImageTk.PhotoImage(img)
        
        self.imageLabel.config(image=imgTk)

    def add_images(self):
        self.manager.add_images()
        self.load_images()

    def view_next(self):
        if self.images and self.atualIndex < len(self.images) - 1:
            self.atualIndex += 1 
        else:
            self.atualIndex = 0
        self.load_images()

    def view_prev(self):
        if self.images and self.atualIndex > 0:
            self.atualIndex -= 1 
        else:
            self.atualIndex = len(self.images) - 1
        self.load_images()
