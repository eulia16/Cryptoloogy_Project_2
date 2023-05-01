from PyQt6.QtGui import QFont, QPixmap, QImage
from PyQt6.QtWidgets import *
import sys

#import Affine
#import SDES

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
        # self.button1.setCheckable(True)

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

        self.button4 = QPushButton()
        self.button4.setText("Advanced Encryption Standard (AES)")
        self.button4.setFont(QFont('Arial', 17))
        self.button4.setStyleSheet('QPushButton {background-color: darkBlue; color: white;}')
        self.button4.clicked.connect(self.show_aes_window)

        self.button5 = QPushButton()
        self.button5.setText("Vigenère Cipher")
        self.button5.setFont(QFont('Arial', 17))
        self.button5.setStyleSheet('QPushButton {background-color: darkBlue; color: white;}')
        self.button5.clicked.connect(self.show_vc_window)

        self.label2 = QLabel("Click one to analyze & implement each symmetric encryption system!")
        self.label2.setFont(QFont('Times', 25))

        # create layouts and add widgets
        hbox = QHBoxLayout()
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.button4)
        hbox2.addWidget(self.button5)

        layout = QVBoxLayout()
        layout.addWidget(picLabel)
        layout.addWidget(self.label1)
        layout.addLayout(hbox)
        layout.addLayout(hbox2)
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

    def show_aes_window(self):
        self.aesWindow = aesWindow()
        self.aesWindow.show()

    def show_vc_window(self):
        self.vcWindow = vcWindow()
        self.vcWindow.show()


class ccWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.cc_popUp()

    def cc_popUp(self):
        self.setWindowTitle("Caesar Cipher")
        self.setFixedSize(800, 650)
        self.setStyleSheet("background-color: beige; color: black")

        self.lbl1 = QLabel("Encode/Decode A Message With The Caesar Cipher")
        self.lbl1.setFont(QFont('Times', 30))
        self.lbl1.setStyleSheet("font-weight: bold")
        self.lbl1.setFixedHeight(30)

        self.plainTextLabel = QLabel(self)
        self.plainTextLabel.setText("Enter a string text to encrypt: ")
        self.plainTextOutput = QLineEdit(self)
        self.plainTextOutput.setPlaceholderText("(e.g., Arrive at threePM)")
        self.plainTextOutput.setStyleSheet("border: 1px solid black;")

        self.keyLabel = QLabel(self)
        self.keyLabel.setText("Enter a number for the key shift (1-26): ")
        self.keyLabelOutput = QLineEdit(self)
        self.keyLabelOutput.setPlaceholderText("Enter # here...")
        self.keyLabelOutput.setStyleSheet("border: 1px solid black;")

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

        layout.addWidget(self.lbl1)
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
        self.plainTextOutput.setFocus()


class acWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ac_popUp()

    def ac_popUp(self):
        self.setWindowTitle("Affine Cipher")
        self.setFixedSize(800, 650)
        self.setStyleSheet("background-color: beige; color: black")

        self.lbl1 = QLabel("The Affine Cipher")
        self.lbl1.setFont(QFont('Times', 30))
        self.lbl1.setStyleSheet("font-weight: bold")
        self.lbl1.setFixedHeight(30)

        self.plainTextLabel = QLabel(self)
        self.plainTextLabel.setText("Enter a string text to encrypt: ")
        self.plainText = QLineEdit(self)
        self.plainText.setPlaceholderText("(e.g., The meeting is at nineAM)  ")
        self.plainText.setStyleSheet("border: 1px solid black;")

        self.aCoefLbl = QLabel(self)
        self.aCoefLbl.setText("Enter your 'a' coefficient: ")
        self.aCoef = QLineEdit(self)
        self.aCoef.setPlaceholderText("Enter # here... ")
        self.aCoef.setStyleSheet("border: 1px solid black;")

        self.bCoefLbl = QLabel(self)
        self.bCoefLbl.setText("Enter your 'b' coefficient: ")
        self.bCoef = QLineEdit(self)
        self.bCoef.setPlaceholderText("Enter # here... ")
        self.bCoef.setStyleSheet("border: 1px solid black;")

        self.btn1 = QPushButton()
        self.btn1.setText("Encrypt")
        self.btn1.setFont(QFont('Arial', 17))
        self.btn1.setStyleSheet('QPushButton {background-color: darkBlue; color: white;}')
        self.btn1.clicked.connect(self.encrypted_text)

        self.encLabel = QLabel(self)
        self.encLabel.setText("Encrypted text: ")
        self.encText = QLineEdit(self)
        self.encText.setStyleSheet("border: 3px solid darkBlue;")
        self.encText.setReadOnly(True)

        self.btn2 = QPushButton()
        self.btn2.setText("Decrypt")
        self.btn2.setFont(QFont('Arial', 17))
        self.btn2.setStyleSheet('QPushButton {background-color: darkBlue; color: white;}')
        # self.button2.clicked.connect(self.decrypted_text)

        self.btn3 = QPushButton()
        self.btn3.setText("Click to Clear and Try again!")
        self.btn3.setFont(QFont('Arial', 17))
        self.btn3.setStyleSheet('QPushButton {background-color: darkBlue; color: white;}')
        self.btn3.clicked.connect(self.clear)

        self.decLabel = QLabel(self)
        self.decLabel.setText("Plaintext: ")
        self.decText = QLineEdit(self)
        self.decText.setStyleSheet("border: 3px solid darkBlue;")
        self.decText.setReadOnly(True)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.plainTextLabel)
        hbox1.addWidget(self.plainText)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.aCoefLbl)
        hbox2.addWidget(self.aCoef)
        hbox2.addWidget(self.bCoefLbl)
        hbox2.addWidget(self.bCoef)

        hbox3 = QHBoxLayout()
        hbox3.addWidget(self.encLabel)
        hbox3.addWidget(self.encText)

        hbox4 = QHBoxLayout()
        hbox4.addWidget(self.decLabel)
        hbox4.addWidget(self.decText)

        layout = QVBoxLayout()
        layout.addWidget(self.lbl1)
        layout.addLayout(hbox1)
        layout.addLayout(hbox2)
        layout.addWidget(self.btn1)
        layout.addLayout(hbox3)
        layout.addWidget(self.btn2)
        layout.addLayout(hbox4)
        layout.addWidget(self.btn3)
        self.setLayout(layout)

    def encrypted_text(self):
        text = self.plainText.text()
        key = [self.aCoef.text(), self.bCoef.text()]
        # print(text, key)

        #self.encText.setText(Affine.affine_encrypt(text, key))

    def decrypted_text(self):
        print(" ")

    def clear(self):
        self.plainText.clear()
        self.aCoef.clear()
        self.bCoef.clear()
        self.encText.clear()
        self.decText.clear()
        self.plainText.setFocus()


class SdesWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.sDes_popUp()

    def sDes_popUp(self):
        self.setWindowTitle("S-DES")
        self.setFixedSize(1050, 750)
        self.setStyleSheet("background-color: beige; color: black")

        self.label1 = QLabel("The Simplified Data Encryption Standard (S-DES) Algorithm")
        self.label1.setFont(QFont('Times', 30))
        self.label1.setStyleSheet("font-weight: bold")
        self.label1.setFixedHeight(35)
        self.label1.setFixedWidth(800)

        self.plainTextLabel = QLabel(self)
        self.plainTextLabel.setText("Enter an 8 bit block of plaintext: ")
        self.plainText = QLineEdit(self)
        self.plainText.setPlaceholderText("(e.g., 10110101)")
        self.plainText.setStyleSheet("border: 1px solid black")

        self.keyLabel = QLabel(self)
        self.keyLabel.setText("Enter a 10 bit block key: ")
        self.key = QLineEdit(self)
        self.key.setPlaceholderText("(e.g., 1011010101)")
        self.key.setStyleSheet("border: 1px solid black")

        self.cipherTxtLbl = QLabel(self)
        self.cipherTxtLbl.setText("Enter an 8 bit block of ciphertext (For decryption): ")
        self.cipherTxt = QLineEdit(self)
        self.cipherTxt.setPlaceholderText("(e.g., 10110101)")
        self.cipherTxt.setStyleSheet("border: 1px solid black")

        self.descBox1 = QPlainTextEdit(self)
        self.descBox1.setFixedHeight(200)
        # self.descBox.setFixedWidth(700)
        self.descBox1.setFont(QFont('Times', 20))
        self.descBox1.setStyleSheet("border: 5px solid white")
        self.descBox1.setReadOnly(True)
        self.descBox1.setPlainText("         S-DES is a model cipher intended for learning. The encryption algorithm takes an "
                                   "8-bit block of plaintext and a 10-bit key as input and produces an 8-bit block of "
                                   "ciphertext. It's a comprehensible version of the full Data Encryption "
                                   "Standard (DES) algorithm, which uses a key size of 56 bits and "
                                   "operates on 64-bit blocks of plaintext. It has the same structures as DES and "
                                   "uses the same notations. DES was developed by IBM with help from the NSA and "
                                   "was one of the most used encryption systems in the world. In S-DES there's a "
                                   "function that's applied twice, whereas in DES, that function is repeated 16 "
                                   "times.  \n\n "
                                   "        Since S-DES is a symmetric cipher, it relies on the use of a 10-bit key shared "
                                   "between the sender and receiver. Two 8-bit subkeys are produced in the key "
                                   "generation for use in separate stages of the encryption and decryption algorithm. "
                                   "The key is first put through a fixed permutation table (P10). Then a "
                                   "shift operation is performed. The P8 operation permutes the 10-bit input"
                                   "key after a function performs a and produces a 8-bit block, known as the subkeys "
                                   "K1 and K2. The cipher involves five functions: an initial permutation (IP); a "
                                   "compounded function labeled fk, which involves both permutation and substitution "
                                   "operations on a string of bits and a subkey; another permutation function that "
                                   "divides the output key into two halves; the fk function again; and a final "
                                   "permutation function that is the inverse of the initial permutation.")

        self.descBox2 = QPlainTextEdit(self)
        self.descBox2.setFixedSize(500, 300)
        # self.descBox.setFixedWidth(700)
        self.descBox2.setFont(QFont('Times', 20))
        self.descBox2.setReadOnly(True)
        self.descBox2.setStyleSheet("border: 5px solid white")
        self.descBox2.setPlainText(
            "The following are the S-DES steps: "
            "\n\nKey Generation process "
            "\n        1. Select random key of 10 bits "
            "\n        2. Put key in P10 table and permute the bits "
            "\n        3. Divide the output key into two halves, left and right"
            "\n        4. Apply the one bit round shift on each half"
            "\n        5. Combine both halves of the bits, right and left. Put them into the P8 function and obtain first "
            "subkey K1 "
            "\n        6. Take the output of the first round shift in step 4"
            "\n        7. Now just apply two round shifts circulate on each half of the bits. Changes the position of two "
            "bits of each halves. "
            "\n        8. Now put the bits into the P8 function and retain your second subkey K2 "
            )

        picLabel = QLabel(self)
        self.sdes_img = QPixmap('../csc 332/sdes.png')
        self.sdes_img.width()
        picLabel.setScaledContents(True)
        # picLabel.resize(300, 300)
        picLabel.setFixedSize(500, 300)
        picLabel.setPixmap(self.sdes_img)

        self.btn1 = QPushButton(self)
        self.btn1.setText("Encrypt")
        self.btn1.setFont(QFont('Arial', 17))
        self.btn1.setStyleSheet('QPushButton {background-color: darkBlue; color: white;}')
        # self.btn1.clicked.connect(self.encrypted_text())

        self.btn2 = QPushButton(self)
        self.btn2.setText("Decrypt")
        self.btn2.setFont(QFont('Arial', 17))
        self.btn2.setStyleSheet('QPushButton {background-color: darkBlue; color: white;}')

        self.encLabel = QLabel(self)
        self.encLabel.setText("Encrypted text: ")
        self.encText = QLineEdit(self)
        self.encText.setStyleSheet("border: 3px solid darkBlue;")
        self.encText.setReadOnly(True)

        self.decLabel = QLabel(self)
        self.decLabel.setText("Decrypted text: ")
        self.decText = QLineEdit(self)
        self.decText.setStyleSheet("border: 3px solid darkBlue;")
        self.decText.setReadOnly(True)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.plainTextLabel)
        hbox1.addWidget(self.plainText)
        hbox1.addWidget(self.keyLabel)
        hbox1.addWidget(self.key)
        hbox1.addWidget(self.cipherTxtLbl)
        hbox1.addWidget(self.cipherTxt)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.btn1)
        hbox2.addWidget(self.btn2)

        hbox3 = QHBoxLayout()
        hbox3.addWidget(self.encLabel)
        hbox3.addWidget(self.encText)
        hbox3.addWidget(self.decLabel)
        hbox3.addWidget(self.decText)

        hbox4 = QHBoxLayout()
        hbox4.addWidget(self.descBox2)
        hbox4.addWidget(picLabel)


        layout = QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addLayout(hbox1)
        layout.addLayout(hbox2)
        layout.addLayout(hbox3)
        layout.addWidget(self.descBox1)
        layout.addLayout(hbox4)
        self.setLayout(layout)


class aesWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.aes_popUp()

    def aes_popUp(self):
        self.setWindowTitle("AES")
        self.resize(800, 600)
        self.setStyleSheet("background-color: beige; color: black")

        self.lbl1 = QLabel("Aes Encryption System")
        self.lbl1.setFont(QFont('Times', 30))
        self.lbl1.setStyleSheet("font-weight: bold")
        self.lbl1.setFixedWidth(700)
        self.lbl1.setFixedHeight(30)

        layout = QVBoxLayout()
        layout.addWidget(self.lbl1)
        self.setLayout(layout)


class vcWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.vc_popUp()

    def vc_popUp(self):
        self.setWindowTitle("Vigenère Cipher")
        self.setFixedSize(900, 750)
        self.setStyleSheet("background-color: beige; color: black")

        self.lbl1 = QLabel("The Vigenère Cipher")
        self.lbl1.setFont(QFont('Times', 30))
        self.lbl1.setStyleSheet("font-weight: bold")
        self.lbl1.setFixedHeight(50)

        self.plainTextLabel = QLabel(self)
        self.plainTextLabel.setText("Enter a string text to encrypt: ")
        self.plainText = QLineEdit(self)
        self.plainText.setPlaceholderText("(e.g., Meet at the Bookstore)")
        self.plainText.setStyleSheet("border: 1px solid black;")

        self.keyLbl = QLabel(self)
        self.keyLbl.setText("Enter your key: ")
        self.key = QLineEdit(self)
        self.key.setPlaceholderText("(e.g., JUNE)")
        self.key.setStyleSheet("border: 1px solid black;")

        self.descBox = QPlainTextEdit(self)
        #self.descBox.setFixedSize(500, 300)
        self.descBox.setFixedHeight(300)
        # self.descBox.setFixedWidth(700)
        self.descBox.setFont(QFont('Times', 20))
        self.descBox.setReadOnly(True)
        self.descBox.setStyleSheet("border: 5px solid white")
        self.descBox.setPlainText("        Named after Blaise de Vigenère, a French cryptographer, the Vigenère cipher is an "
                                  "expanded Caesar Cipher where a message is encrypted "
                                  "using a series of different Caesar Ciphers, based on the letters of a specific "
                                  "keyword. The length of the keyword determines the "
                                  "number of different encryptions that are applied to the plaintext."
                                  "\n\n          To encrypt, you use a table of alphabets, known as a Vigenère "
                                  "table. It "
                                  "consist of the alphabet written 26 times in different rows, with each alphabet "
                                  "shifted periodically to the left compared to the one in the row above, as shown in "
                                  "the figure. To decrypt the ciphertext, you have "
                                  "to know the key that was used, and work backwards through the encryption procedure. "
                                  "The concept behind the Vigenère cipher is to hide the plaintext letter frequencies "
                                  "to increases the security of your message.")

        picLabel = QLabel(self)
        self.vc_img = QPixmap('../csc 332/vc_img.jpeg')
        self.vc_img.width()
        picLabel.setScaledContents(True)
        # picLabel.resize(300, 300)
        picLabel.setFixedSize(425, 300)
        picLabel.setPixmap(self.vc_img)


        self.btn1 = QPushButton()
        self.btn1.setText("Encrypt")
        self.btn1.setFont(QFont('Arial', 17))
        self.btn1.setStyleSheet('QPushButton {background-color: darkBlue; color: white;}')
        # self.button1.clicked.connect(self.encrypted_text)

        self.encLabel = QLabel(self)
        self.encLabel.setText("Encoded Message: ")
        self.encText = QLineEdit(self)
        self.encText.setStyleSheet("border: 3px solid darkBlue;")
        self.encText.setReadOnly(True)

        self.btn2 = QPushButton()
        self.btn2.setText("Decrypt")
        self.btn2.setFont(QFont('Arial', 17))
        self.btn2.setStyleSheet('QPushButton {background-color: darkBlue; color: white;}')
        # self.button2.clicked.connect(self.decrypted_text)

        self.btn3 = QPushButton()
        self.btn3.setText("Click to Clear and Try again!")
        self.btn3.setFont(QFont('Arial', 17))
        self.btn3.setStyleSheet('QPushButton {background-color: darkBlue; color: white;}')
        self.btn3.clicked.connect(self.clear)

        self.decLabel = QLabel(self)
        self.decLabel.setText("Decoded message: ")
        self.decText = QLineEdit(self)
        self.decText.setStyleSheet("border: 3px solid darkBlue;")
        self.decText.setReadOnly(True)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.plainTextLabel)
        hbox1.addWidget(self.plainText)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.keyLbl)
        hbox2.addWidget(self.key)

        hbox3 = QHBoxLayout()
        hbox3.addWidget(self.encLabel)
        hbox3.addWidget(self.encText)

        hbox4 = QHBoxLayout()
        hbox4.addWidget(self.decLabel)
        hbox4.addWidget(self.decText)

        hbox5 = QHBoxLayout()
        hbox5.addWidget(self.descBox)
        hbox5.addWidget(picLabel)

        layout = QVBoxLayout()
        layout.addWidget(self.lbl1)
        layout.addLayout(hbox1)
        layout.addLayout(hbox2)
        layout.addWidget(self.btn1)
        layout.addLayout(hbox3)
        layout.addWidget(self.btn2)
        layout.addLayout(hbox4)
        layout.addLayout(hbox5)
        layout.addWidget(self.btn3)
        self.setLayout(layout)

    def clear(self):
        self.plainText.clear()
        self.key.clear()
        self.encText.clear()
        self.decText.clear()
        self.plainText.setFocus()


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
