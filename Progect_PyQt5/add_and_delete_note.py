from random import randint

import os
import shutil


class NewNote:
    def __init__(self):
        self.file_name = ''

    def add_note(self):
        file_name = open('files/name_files.txt', mode='a')
        name = f'{randint(1, 1000)}'
        self.file_name = name
        os.mkdir(f'files/{name}')
        title = open(f'files/{name}/title.txt', mode='a')
        title.write('')
        title.close()
        genre = open(f'files/{name}/genre.txt', mode='a')
        genre.write('')
        genre.close()
        description = open(f'files/{name}/description.txt', mode='a')
        description.write('')
        description.close()
        file_name.write(f'{name}\n')
        file_name.close()
        return self.__str__()

    def __str__(self):
        return self.file_name


class DeleteNote:
    def __init__(self, file_name):
        self.file_name = file_name
        self.new_data_file_name = []

    def delete_file(self):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), f'files/{self.file_name}')
        shutil.rmtree(path)
        with open('files/name_files.txt') as f:
            file = f.readlines()
            self.new_data_file_name = file
        self.new_data_file_name.remove(str(self.file_name) + '\n')
        file = open('files/name_files.txt', mode='w')
        file.close()
        file = open('files/name_files.txt', mode='a')
        for i in self.new_data_file_name:
            file.write(i)
        file.close()
