from PIL import Image
from PyQt6.QtGui import QFont, QPixmap, QImage
from PyQt6.QtWidgets import *
import sys
import sage

from PyQt6.uic.properties import QtGui, QtWidgets


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Encryption Systems")
        self.setFixedSize(800, 750)
        self.setStyleSheet("background-color: gray; color: white")

        picLabel = QLabel(self)
        self.logo = QPixmap('../csc 332/coverImg.jpeg')
        self.logo.width()
        picLabel.setScaledContents(True)
        # picLabel.resize(300, 300)
        picLabel.setPixmap(self.logo)

        self.label1 = QLabel("Learning Cryptography Through Programming in Python")
        self.label1.setFont(QFont('Times', 30))

        # widgets
        self.button1 = QPushButton()
        self.button1.setText("Caesar Cipher")
        self.button1.setFont(QFont('Arial', 17))
        self.button1.setStyleSheet('QPushButton {background-color: darkBlue; color: white;}')
        self.button1.clicked.connect(self.show_cc_window)

        self.button2 = QPushButton()
        self.button2.setText("Affine Cipher")
        self.button2.setFont(QFont('Arial', 17))
        self.button2.setStyleSheet('QPushButton {background-color: darkBlue; color: white;}')
        self.button2.clicked.connect(self.show_ac_window)

        self.button3 = QPushButton()
        self.button3.setText("Simplified Data Encryption Standard (S-DES)")
        self.button3.setFont(QFont('Arial', 17))
        self.button3.setStyleSheet('QPushButton {background-color: darkBlue; color: white;}')
        self.button3.clicked.connect(self.show_sDes_window)

        self.label2 = QLabel("Click one to analyze each symmetric encryption system!")
        self.label2.setFont(QFont('Times', 25))

        # create layouts and add widgets
        hbox = QHBoxLayout()
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)

        layout = QVBoxLayout()
        layout.addWidget(picLabel)
        layout.addWidget(self.label1)
        layout.addLayout(hbox)
        layout.addWidget(self.button3)
        layout.addWidget(self.label2)
        self.setLayout(layout)

    # create pop up window
    def show_cc_window(self):
        self.ccWindow = ccWindow()
        self.ccWindow.show()

    def show_ac_window(self):
        self.acWindow = acWindow()
        self.acWindow.show()

    def show_sDes_window(self):
        self.sDesWindow = SdesWindow()
        self.sDesWindow.show()


class ccWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.cc_popUp()

    def cc_popUp(self):
        self.setWindowTitle("Caesar Cipher")
        self.resize(800, 600)
        #self.setStyleSheet("background-color: gray; color: white")

        self.plainTextLabel = QLabel(self)
        self.plainTextLabel.setText("Enter a string text to encrypt: ")
        self.plainTextOutput = QLineEdit(self)
        # self.plainTextOutput.cursor()

        self.keyLabel = QLabel(self)
        self.keyLabel.setText("Enter a number for the key shift (1-26): ")
        self.keyLabelOutput = QLineEdit(self)
        # self.keyLabelOutput.setStyleSheet("border: 3px solid darkBlue;")

        self.button1 = QPushButton()
        self.button1.setText("Encrypt")
        self.button1.setFont(QFont('Arial', 17))
        self.button1.setStyleSheet('QPushButton {background-color: darkBlue; color: white;}')
        self.button1.clicked.connect(self.encrypted_text)

        self.encLabel = QLabel(self)
        self.encLabel.setText("Encrypted text: ")
        self.encText = QLineEdit(self)
        self.encText.setStyleSheet("border: 3px solid darkBlue;")
        self.encText.setReadOnly(True)

        self.button2 = QPushButton()
        self.button2.setText("Decrypt")
        self.button2.setFont(QFont('Arial', 17))
        self.button2.setStyleSheet('QPushButton {background-color: darkBlue; color: white;}')
        self.button2.clicked.connect(self.decrypted_text)

        self.button3 = QPushButton()
        self.button3.setText("Click to Clear and Try again!")
        self.button3.setFont(QFont('Arial', 17))
        self.button3.setStyleSheet('QPushButton {background-color: darkBlue; color: white;}')
        self.button3.clicked.connect(self.clear)

        self.decLabel = QLabel(self)
        self.decLabel.setText("Plaintext: ")
        self.decText = QLineEdit(self)
        self.decText.setStyleSheet("border: 3px solid darkBlue;")
        self.decText.setReadOnly(True)

        hbox = QHBoxLayout()
        hbox.addWidget(self.plainTextLabel)
        hbox.addWidget(self.plainTextOutput)
        hbox.addWidget(self.keyLabel)
        hbox.addWidget(self.keyLabelOutput)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.encLabel)
        hbox2.addWidget(self.encText)
        # hbox2.addWidget(self.button2)

        hbox3 = QHBoxLayout()
        hbox3.addWidget(self.decLabel)
        hbox3.addWidget(self.decText)

        layout = QVBoxLayout()
        layout.addLayout(hbox)
        layout.addWidget(self.button1)
        layout.addLayout(hbox2)
        layout.addWidget(self.button2)
        layout.addLayout(hbox3)
        layout.addWidget(self.button3)
        self.setLayout(layout)

    def encrypted_text(self):
        self.encText.setText(self.cipher(self.plainTextOutput.text(), self.keyLabelOutput.text(), False))

    def decrypted_text(self):
        self.encypted_value = self.cipher(self.plainTextOutput.text(), self.keyLabelOutput.text(), False)

        self.decText.setText(self.cipher(self.encypted_value, self.keyLabelOutput.text(), True))

    def cipher(self, message, key, is_encrypted):

        key = int(key)

        if is_encrypted:
            key = -key

        translated = ''
        for symbol in message:
            if symbol.isalpha():
                num = ord(symbol)
                num += key

                if symbol.isupper():
                    if num > ord('Z'):
                        num -= 26
                    elif num < ord('A'):
                        num += 26
                elif symbol.islower():
                    if num > ord('z'):
                        num -= 26
                    elif num < ord('a'):
                        num += 26
                translated += chr(num)
                # print(translated)
            else:
                translated += symbol

        return translated

    def clear(self):
        self.plainTextOutput.clear()
        self.keyLabelOutput.clear()
        self.encText.clear()
        self.decText.clear()



class acWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ac_popUp()

    def ac_popUp(self):
        self.setWindowTitle("Affine Cipher")
        self.resize(800, 600)

        self.label1 = QLabel("Affine Cipher in Detail")
        self.label1.setFont(QFont('Times', 30))


class SdesWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.sDes_popUp()

    def sDes_popUp(self):
        self.setWindowTitle("S-DES")
        self.resize(800, 600)

        self.label1 = QLabel("SDES in Detail")
        self.label1.setFont(QFont('Times', 30))

        self.plainTextLabel = QLabel(self)
        self.plainTextLabel.setText("Enter an 8 bit block of plaintext (e.g., 10110101): ")
        self.plainTextOutput = QLineEdit(self)

        self.keyLabel = QLabel(self)
        self.keyLabel.setText("Enter a 10 bit block key (e.g., 1011010101): ")
        self.keyOutput = QLineEdit(self)

        hbox = QHBoxLayout()
        hbox.addWidget(self.plainTextLabel)
        hbox.addWidget(self.plainTextOutput)
        hbox.addWidget(self.keyLabel)
        hbox.addWidget(self.keyOutput)

        layout = QVBoxLayout()
        layout.addLayout(hbox)
        layout.addWidget(self.label1)
        self.setLayout(layout)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
