import sys

import numpy as np
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication

import UI


# class sow(QtWidgets.QMainWindow):
#     def __init__(self, parent=None):
#         QtWidgets.QMainWindow.__init__(self, parent)
#
#         self.main_ui = UI.Ui_MainWindow()
#         self.main_ui.setupUi(self)
#         self.main_ui.encryptionButton.clicked.connect(self.enClicked)
#
#     def enClicked(self):
#         # text=str(self.encrypter.text())
#         # key=int(self.enKey.text())
#         # enText=encoder(text, key)
#         # self.encrypted.setText(enText)
#

def encoder(word, key):
    modword = word.replace(" ", "")
    if not modword.isalpha(): return "Unacceptable input"
    wordascii = np.array([ord(c) for c in modword.lower()])
    wordencryption = (((wordascii - 97) + key) % 26) + 97
    encryption = [chr(c) for c in wordencryption]
    return ''.join(encryption)


def decoder(word, key):
    wordascii = np.array([ord(c) for c in word.lower()])
    worddecryption = (((wordascii - 97) - key) % 26) + 97
    decryption = [chr(c) for c in worddecryption]
    return ''.join(decryption)


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = UI.Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()


def main():
    app = QApplication(sys.argv)
    instance = Main()
    #myapp = sow()
    #myapp.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
    encrypted = encoder('Py     Charm', 3)
    print(encrypted)
    decrypted = decoder(encrypted, 3)
    print(decrypted)
