import os
import shutil
from tkinter import filedialog

class ImageManager:
    def __init__ (self, destinationFolder="images"):
        self.destinationFolder = destinationFolder
        self.images = []

        if not os.path.exists(self.destinationFolder):
            os.makedirs(self.destinationFolder)
        self.load_images()

    def add_images(self):
        files = filedialog.askopenfilenames(
            title = "Selecione as imagens",
            filetypes=[("Imagens", "*.png *.jpg *.jpeg *.gif *.bmp"), ("Todos os arquivos", "*.*")]
        )

        if not files:
            return []

        savedPaths = []
        for file in files:
            filename = os.path.basename(file)
            destination = os.path.join(self.destinationFolder, filename)

            shutil.copy(file, destination)
            savedPaths.append(destination)

        self.load_images()
        return savedPaths

    def load_images(self):
        self.images = []
        for img in os.listdir(self.destinationFolder):
            if img.lower().endswith(('png', 'jpg', 'jpeg', 'gif', 'bmp')):
                fullPath = os.path.join(self.destinationFolder, img)
                self.images.append(fullPath)
    
    def list_images(self):
        return self.images
