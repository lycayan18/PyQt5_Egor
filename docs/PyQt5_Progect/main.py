import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import uic


from py import my_form
from add_and_delete_note import NewNote, DeleteNote
import os


class Example(QWidget, my_form.Ui_Form):
    def __init__(self):
        super().__init__()
        self.file_name = ''
        self.new_data_file_name = []
        self.initUI()

    def initUI(self):
        uic.loadUi('Menu.ui', self)
        self.window().showFullScreen()
        self.setWindowTitle('NFF')
        self.hide_or_show_widgets(True)
        self.pushButton.clicked.connect(self.add_note)
        self.pushButton_2.clicked.connect(self.delete_button)
        self.pushButton_5.clicked.connect(self.exit_file)
        icon = QIcon()
        icon.addPixmap(QPixmap("img/trash-can-2.png"))
        self.pushButton_2.setIcon(icon)
        icon = QIcon()
        icon.addPixmap(QPixmap("img/free-icon-add-to-favorites-4989206-2.png"))
        self.pushButton_3.setIcon(icon)
        icon = QIcon()
        icon.addPixmap(QPixmap("img/back-2.png"))
        self.pushButton_5.setIcon(icon)
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
        self.hide_or_show_widgets(False)
        self.lineEdit.setText('Title:')
        self.lineEdit_2.setText('Genre:')
        self.textEdit.setText('Description:')
        self.label.hide()

    def handler_clicks(self, value):
        def handler():
            self.click_note(value)

        return handler

    def add_note(self):
        new_note = NewNote()
        new_note.add_note()
        self.file_name = new_note
        self.hide_or_show_widgets(False)
        self.label.hide()
        self.display()

    def delete_file(self):
        delete_note = DeleteNote(self.file_name)
        delete_note.delete_file()

    def exit_file(self):
        void_checks = {
            1: self.lineEdit.text() == '' or self.lineEdit.text() == 'Title:',
            2: self.lineEdit_2.text() == '' or self.lineEdit_2.text() == 'Genre:',
            3: self.textEdit.toPlainText() == '' or self.textEdit.toPlainText() == 'Description:',
        }
        if void_checks[1] and void_checks[2] and void_checks[3]:
            self.delete_file()
            self.display()
        self.hide_or_show_widgets(True)
        self.label.show()

    def delete_button(self):
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = Example()
    widget.show()
    sys.exit(app.exec())