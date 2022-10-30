from add_and_delete_note import DeleteNote
import os


class CheckingFiles:
    def __init__(self):
        self.files = open('files/name_files.txt', mode='rt')
        self.check_title = False
        self.check_genre = False
        self.check_description = False
        self.check_img = False

    def check(self):
        for i in self.files.readlines():
            name_file = i[:-1]
            title = open(f'files/{name_file}/title.txt', mode='rt')
            if len(title.readlines()) > 0:
                self.check_title = True
            else:
                self.check_title = False
            title.close()

            genre = open(f'files/{name_file}/genre.txt', mode='rt')
            if len(genre.readlines()) > 0:
                self.check_genre = True
            else:
                self.check_genre = False
            genre.close()

            description = open(f'files/{name_file}/description.txt', mode='rt')
            if len(description.readlines()) > 0:
                self.check_description = True
            else:
                self.check_description = False
            description.close()
            if os.path.isfile(f'files/{name_file}/img.png'):
                self.check_img = True
            else:
                self.check_img = False
            check = {
                1: self.check_title is False,
                2: self.check_genre is False,
                3: self.check_description is False,
                4: self.check_img is False

            }
            if check[1] and check[2] and check[3] and check[4]:
                delete = DeleteNote(name_file)
                delete.delete_file()
        self.files.close()
