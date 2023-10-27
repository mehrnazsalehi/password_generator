from PyQt5.QtWidgets import QMainWindow, QApplication, QCheckBox, QLabel, QPushButton, QSlider, QLineEdit, QMessageBox
from PyQt5 import uic
import sys
from random import randint


class UI(QMainWindow):

    def __init__(self):
        super(UI, self).__init__()

        self.uppercase = False
        self.my_password = None
        self.password_length = None
        uic.loadUi("password_generator.ui", self)

        self.titlelabel = self.findChild(QLabel, "titlelabel")
        self.lineEdit = self.findChild(QLineEdit, "lineEdit")
        self.copyButton = self.findChild(QPushButton, "copyButton")
        self.horizontalSlider = self.findChild(QSlider, "horizontalSlider")
        self.lengthlabel = self.findChild(QLabel, "lengthlabel")
        self.countlabel = self.findChild(QLabel, "countlabel")
        self.checkBox = self.findChild(QCheckBox, "checkBox")
        self.checkboxlabel = self.findChild(QLabel, "checkboxlabel")
        self.passwordButton = self.findChild(QPushButton, "passwordButton")
        self.length_entry = self.findChild(QLineEdit, "length_entry")

        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(50)

        self.horizontalSlider.valueChanged.connect(self.slide_it)

        self.copyButton.clicked.connect(self.copy_password)

        self.checkBox.toggled.connect(lambda: self.checked())

        self.passwordButton.clicked.connect(self.generate_password)

        self.show()

    def slide_it(self, value):
        length = str(self.horizontalSlider.value())
        self.length_entry.setText(length)

    def checked(self):
        global uppercase
        self.uppercase = False
        if self.checkBox.isChecked():
            self.uppercase = True
        else:
            self.uppercase = False

    def generate_password(self):
        self.my_password = ''
        self.password_length = int(self.length_entry.text())
        for x in range(self.password_length):
            self.my_password += chr(randint(33, 126))
        if self.uppercase:
            self.lineEdit.setText(self.my_password)
        else:
            self.lowercase = self.my_password.lower()
            self.lineEdit.setText(self.lowercase)

    def copy_password(self):
        cb = QApplication.clipboard()
        cb.clear(mode=cb.Clipboard)
        cb.setText(self.lineEdit.text(), mode=cb.Clipboard)
        self.lineEdit.setText("copied!")
        QMessageBox.about(self, "copy message!", f'The password is copied to clipboard')


app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
