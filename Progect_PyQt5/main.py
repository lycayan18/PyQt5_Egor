import sys
from PIL import Image
import os

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QFileDialog, QMessageBox, QDialog
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import uic

from py import my_form, my_form_favourites
from add_and_delete_note import NewNote, DeleteNote
from data_note import AddData
from checking_empty_files import CheckingFiles
from sorting_notes import SortingNormal, SortingName
from add_and_delete_note_favourites import AddNoteFavourites, DeleteNoteFavourites


class Example(QWidget, my_form.Ui_Form):
    def __init__(self):
        super().__init__()
        self.file_name = ''
        self.new_data_file_name = []
        self.img = ''
        self.initializer()

    def initializer(self):
        uic.loadUi('Menu.ui', self)
        self.window().showFullScreen()
        self.setWindowTitle('NoteFilms')
        self.hide_or_show_widgets(True)
        self.pushButton.clicked.connect(self.add_note)
        self.pushButton_2.clicked.connect(self.delete_button)
        self.pushButton_3.clicked.connect(self.add_and_delete_favourites_list)
        self.pushButton_4.clicked.connect(self.choose_picture)
        self.pushButton_5.clicked.connect(self.exit_file)
        self.pushButton_6.clicked.connect(self.favourites_window)
        self.comboBox.currentIndexChanged.connect(self.sorting_notes)
        icon = QIcon()
        icon.addPixmap(QPixmap("img/trash-can-2.png"))
        self.pushButton_2.setIcon(icon)
        icon = QIcon()
        icon.addPixmap(QPixmap("img/free-icon-add-to-favorites-4989206-2.png"))
        self.pushButton_3.setIcon(icon)
        icon = QIcon()
        icon.addPixmap(QPixmap("img/back-2.png"))
        self.pushButton_5.setIcon(icon)
        self.lineEdit.setPlaceholderText('Title:')
        self.lineEdit_2.setPlaceholderText('Genre:')
        self.textEdit.setPlaceholderText('Description:')
        self.lineEdit.setMaxLength(59)
        self.lineEdit_2.setMaxLength(59)
        check = CheckingFiles()
        check.check()
        self.display()

    def display(self):
        if os.path.getsize('files/name_files.txt') > 0:
            layout = QGridLayout()
            with open('files/name_files.txt', mode='rt') as f:
                file = f.readlines()
                button_name = file
            for i in button_name:
                name = i.replace('\n', '')
                but1 = QPushButton(name, self)
                but1.show()
                but1.clicked.connect(self.handler_clicks(but1.text()))
                layout.addWidget(but1)
            w = QWidget()
            w.setLayout(layout)
            self.scrollArea.setWidget(w)
        else:
            layout = QGridLayout()
            w = QWidget()
            w.setLayout(layout)
            self.scrollArea.setWidget(w)

    def click_note(self, name):
        self.file_name = name
        self.pushButton.setEnabled(False)
        self.scrollArea.setEnabled(False)
        self.pushButton_6.setEnabled(False)
        self.hide_or_show_widgets(False)
        self.label.hide()
        self.display_data_file()

    def handler_clicks(self, value):
        def handler():
            self.click_note(value)

        return handler

    def add_note(self):
        new_note = NewNote()
        new_note.add_note()
        icon = QIcon()
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setText('Select File')
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
        self.textEdit.setText('')
        icon = QIcon()
        icon.addPixmap(QPixmap("img/free-icon-add-to-favorites-4989206-2.png"))
        self.pushButton_3.setIcon(icon)
        self.pushButton.setEnabled(False)
        self.scrollArea.setEnabled(False)
        self.pushButton_6.setEnabled(False)
        self.hide_or_show_widgets(False)
        self.label.hide()
        self.file_name = str(new_note)
        self.display()

    def delete_file(self):
        delete_note = DeleteNote(self.file_name)
        delete_note.delete_file()
        self.pushButton_6.setEnabled(True)

    def exit_file(self):
        void_checks = {
            1: self.lineEdit.text() == '',
            2: self.lineEdit_2.text() == '',
            3: self.textEdit.toPlainText() == '',
            4: self.img == '' and os.path.isfile(f'files/{self.file_name}/img.png') is False
        }
        if void_checks[1] and void_checks[2] and void_checks[3] and void_checks[4]:
            self.delete_file()
            self.display()
        self.add_data_note()
        self.pushButton.setEnabled(True)
        self.scrollArea.setEnabled(True)
        self.pushButton_6.setEnabled(True)
        self.hide_or_show_widgets(True)
        self.label.show()
        self.img = ''
        self.sorting_notes()

    def add_data_note(self):
        title = self.lineEdit.text()
        genre = self.lineEdit_2.text()
        description = self.textEdit.toPlainText()
        data = AddData(self.file_name, title, genre, description, self.img)
        data.add_data()

    def display_data_file(self):
        title = open(f'files/{self.file_name}/title.txt', mode='rt')
        self.lineEdit.setText(title.readline())
        title.close()
        genre = open(f'files/{self.file_name}/genre.txt', mode='rt')
        self.lineEdit_2.setText(genre.readline())
        genre.close()
        description = open(f'files/{self.file_name}/description.txt', mode='rt')
        self.textEdit.setText(description.read())
        genre.close()
        if os.path.isfile(f'files/{self.file_name}/img.png'):
            icon = QIcon()
            icon.addPixmap(QPixmap(f'files/{self.file_name}/img.png'))
            self.pushButton_4.setText('')
            self.pushButton_4.setIcon(icon)
        else:
            icon = QIcon()
            self.pushButton_4.setIcon(icon)
            self.pushButton_4.setText('Select File')
        favourites = open(f'files/{self.file_name}/favourites.txt', mode='rt')
        value = favourites.readline()
        if value == 'True':
            icon = QIcon()
            icon.addPixmap(QPixmap("img/free-icon-add-to-favorites-4989206-2-2.png"))
            self.pushButton_3.setIcon(icon)
        else:
            icon = QIcon()
            icon.addPixmap(QPixmap("img/free-icon-add-to-favorites-4989206-2.png"))
            self.pushButton_3.setIcon(icon)

    def delete_button(self):
        self.pushButton.setEnabled(True)
        self.scrollArea.setEnabled(True)
        self.hide_or_show_widgets(True)
        self.label.show()
        self.delete_file()
        self.display()

    def hide_or_show_widgets(self, cmd):
        if cmd:
            self.pushButton_2.hide()
            self.pushButton_3.hide()
            self.pushButton_4.hide()
            self.pushButton_5.hide()
            self.lineEdit.hide()
            self.lineEdit_2.hide()
            self.textEdit.hide()
        else:
            self.pushButton_2.show()
            self.pushButton_3.show()
            self.pushButton_4.show()
            self.pushButton_5.show()
            self.lineEdit.show()
            self.lineEdit_2.show()
            self.textEdit.show()

    def choose_picture(self):
        name, filter_img = QFileDialog.getOpenFileName(self, "Выбор картинки", filter="*.jpg;;*png;;*jpeg")
        if name:
            if os.stat(name).st_size > 0:
                img = Image.open(name)
                img = img.resize((371, 497))
                img.save('img/icon.png')
                icon = QIcon()
                icon.addPixmap(QPixmap('img/icon.png'))
                path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'img/icon.png')
                os.remove(path)
                self.pushButton_4.setText('')
                self.pushButton_4.setIcon(icon)
                self.img = name
            else:
                try:
                    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), f'files/{self.file_name}/img.png')
                    os.remove(path)
                    icon = QIcon()
                    self.pushButton_4.setIcon(icon)
                    QMessageBox.critical(self, "Ошибка ", "Error The file is empty", QMessageBox.Ok)
                    self.pushButton_4.setText('Select File')
                except FileNotFoundError:
                    icon = QIcon()
                    self.pushButton_4.setIcon(icon)
                    QMessageBox.critical(self, "Error ", "Error The file is empty", QMessageBox.Ok)
                    self.pushButton_4.setText('Select File')

    def sorting_notes(self):
        if self.comboBox.currentText() == 'Sorting by editing':
            SortingNormal.sort()
            self.display()
        else:
            SortingName().sort()
            self.display()

    @staticmethod
    def favourites_window():
        op = Favourites()
        op.exec()

    def add_and_delete_favourites_list(self):
        file = open(f'files/{self.file_name}/favourites.txt', mode='rt')
        value = file.readline()
        file.close()
        if value == 'False':
            add = AddNoteFavourites(self.file_name)
            add.add_note()
            icon = QIcon()
            icon.addPixmap(QPixmap("img/free-icon-add-to-favorites-4989206-2-2.png"))
            self.pushButton_3.setIcon(icon)
        else:
            delete = DeleteNoteFavourites(self.file_name)
            delete.delete_note()
            icon = QIcon()
            icon.addPixmap(QPixmap("img/free-icon-add-to-favorites-4989206-2.png"))
            self.pushButton_3.setIcon(icon)


class Favourites(QDialog, my_form_favourites.Ui_Form):
    def __init__(self):
        super().__init__()
        self.initializer()

    def initializer(self):
        uic.loadUi('menu_favourites.ui', self)
        self.window().resize(1042, 631)
        self.window().move(210, 90)
        self.setWindowTitle('Favourites')
        icon = QIcon()
        icon.addPixmap(QPixmap("img/back-2.png"))
        self.pushButton_1.setIcon(icon)
        self.pushButton_1.clicked.connect(self.close_favourites)
        self.display_notes()

    def display_notes(self):
        if os.path.getsize('files/names_files_menu_favourites.txt') > 0:
            layout = QGridLayout()
            with open('files/names_files_menu_favourites.txt', mode='rt') as f:
                file = f.readlines()
                button_name = file
            for i in button_name:
                name = i.replace('\n', '')
                but1 = QPushButton(name, self)
                but1.show()
                layout.addWidget(but1)
            w = QWidget()
            w.setLayout(layout)
            self.scrollArea.setWidget(w)
        else:
            layout = QGridLayout()
            w = QWidget()
            w.setLayout(layout)
            self.scrollArea.setWidget(w)

    def close_favourites(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = Example()
    widget.show()
    sys.exit(app.exec())
