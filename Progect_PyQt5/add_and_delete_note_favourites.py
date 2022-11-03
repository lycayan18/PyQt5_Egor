class AddNoteFavourites:
    def __init__(self, file_name):
        self.file_name = file_name

    def add_note(self):
        file = open(f'files/{self.file_name}/favourites.txt', mode='w')
        file.close()
        file = open(f'files/{self.file_name}/favourites.txt', mode='a')
        file.write('True')
        file.close()
        names_files_favourites = open('files/names_files_menu_favourites.txt', mode='a')
        names_files_favourites.write(f'{self.file_name}\n')
        names_files_favourites.close()


class DeleteNoteFavourites:
    def __init__(self, file_name):
        self.file_name = file_name

    def delete_note(self):
        file = open(f'files/{self.file_name}/favourites.txt', mode='w')
        file.close()
        file = open(f'files/{self.file_name}/favourites.txt', mode='a')
        file.write('False')
        file.close()
        names_files_favourites = open('files/names_files_menu_favourites.txt', mode='rt')
        new_data_names_files_favourites = names_files_favourites.readlines()
        names_files_favourites.close()
        names_files_favourites = open('files/names_files_menu_favourites.txt', mode='w')
        names_files_favourites.close()
        new_data_names_files_favourites.remove(str(self.file_name) + '\n')
        names_files_favourites = open('files/names_files_menu_favourites.txt', mode='a')
        for i in new_data_names_files_favourites:
            names_files_favourites.write(i)
        names_files_favourites.close()
