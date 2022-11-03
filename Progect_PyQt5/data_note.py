from PIL import Image
from datetime import datetime
import os


class AddData:
    def __init__(self, name_file, title, genre, description, img):
        self.name_file = name_file
        self.title = title
        self.genre = genre
        self.description = description
        self.img = img

    def add_data(self):
        if os.path.exists(f'files/{self.name_file}'):
            self.add_title()
            self.add_genre()
            self.add_description()
            self.add_img()
            self.add_editing_time()

    def add_title(self):
        title = open(f'files/{self.name_file}/title.txt', mode='w')
        title.close()
        title = open(f'files/{self.name_file}/title.txt', mode='a')
        title.write(self.title)
        title.close()

    def add_genre(self):
        genre = open(f'files/{self.name_file}/genre.txt', mode='w')
        genre.close()
        genre = open(f'files/{self.name_file}/genre.txt', mode='a')
        genre.write(self.genre)
        genre.close()

    def add_description(self):
        description = open(f'files/{self.name_file}/description.txt', mode='w')
        description.close()
        description = open(f'files/{self.name_file}/description.txt', mode='a')
        description.write(self.description)
        description.close()

    def add_img(self):
        if self.img != '':
            img = Image.open(self.img)
            img = img.resize((371, 497))
            img.save(f'files/{self.name_file}/img.png')

    def add_editing_time(self):
        editing_time = open(f'files/{self.name_file}/editing_time.txt', mode='w')
        editing_time.close()
        editing_time = open(f'files/{self.name_file}/editing_time.txt', mode='a')
        editing_time.write(str(datetime.now()))
        editing_time.close()
