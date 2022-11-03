from random import randint
import os
import shutil


from add_and_delete_note_favourites import DeleteNoteFavourites


class NewNote:
    def __init__(self):
        self.file_name = ''

    def add_note(self):
        file_name = open('files/name_files.txt', mode='rt')
        file_name_list = file_name.readlines()
        file_name.close()
        if len(file_name_list) <= 1000:
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
            editing_time = open(f'files/{name}/editing_time.txt', mode='a')
            editing_time.write('')
            editing_time.close()
            favourites = open(f'files/{name}/favourites.txt', mode='a')
            favourites.write('False')
            favourites.close()
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
        names_files_favourites = open('files/names_files_menu_favourites.txt', mode='rt')
        list_names = names_files_favourites.readlines()
        names_files_favourites.close()
        if str(self.file_name + '\n') in list_names:
            delete = DeleteNoteFavourites(self.file_name)
            delete.delete_note()
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
