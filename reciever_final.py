from PyQt6 import QtCore, QtGui, QtWidgets
import sender_final

class Ui_RecieveWindow(object):

    def sendToSender(self):
        self.ui = sender_final.Ui_SendWindow()
        encrMess = self.R_encryptedTextEdit.text()
        self.ui.S_messagesTextEdit.setText(encrMess)

    def cipher_encrypt(self):
        encrypted = ""
        key = 7
        plain_text = self.R_plainTextEdit.text()
        self.R_plainTextEdit.setText("")
        for c in plain_text:
            if c.isupper(): #check if it's an uppercase character
                c_index = ord(c) - ord('A')
                # shift the current character by key positions
                c_shifted = (c_index + key) % 26 + ord('A')
                c_new = chr(c_shifted)
                encrypted += c_new
            elif c.islower(): #check if its a lowecase character
                # subtract the unicode of 'a' to get index in [0-25) range
                c_index = ord(c) - ord('a') 
                c_shifted = (c_index + key) % 26 + ord('a')
                c_new = chr(c_shifted)
                encrypted += c_new
            elif c.isdigit():
                # if it's a number,shift its actual value 
                c_new = (int(c) + key) % 10
                encrypted += str(c_new)
            else:
                # if its neither alphabetical nor a number, just leave it like that
                encrypted += c

        self.R_encryptedTextEdit.setText(encrypted)
        return encrypted

    def cipher_decrypt(self):
        decrypted = ""
        key = 7
        if self.R_encryptedTextEdit.text():
            ciphertext = self.R_encryptedTextEdit.text()
        else:
            ciphertext = self.R_plainTextEdit.text()
        self.R_encryptedTextEdit.setText("")
        for c in ciphertext:
            if c.isupper(): 
                c_index = ord(c) - ord('A')
                # shift the current character to left by key positions to get its original position
                c_og_pos = (c_index - key) % 26 + ord('A')
                c_og = chr(c_og_pos)
                decrypted += c_og
            elif c.islower(): 
                c_index = ord(c) - ord('a') 
                c_og_pos = (c_index - key) % 26 + ord('a')
                c_og = chr(c_og_pos)
                decrypted += c_og
            elif c.isdigit():
                # if it's a number,shift its actual value 
                c_og = (int(c) - key) % 10
                decrypted += str(c_og)
            else:
                # if its neither alphabetical nor a number, just leave it like that
                decrypted += c
        self.R_plainTextEdit.setText(decrypted)
        return decrypted

    def setupUi(self, SendWindow):
        SendWindow.setObjectName("SendWindow")
        SendWindow.resize(380, 485)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SendWindow.sizePolicy().hasHeightForWidth())
        SendWindow.setSizePolicy(sizePolicy)
        SendWindow.setMinimumSize(QtCore.QSize(380, 450))
        SendWindow.setMaximumSize(QtCore.QSize(380, 500))
        SendWindow.setDocumentMode(True)
        self.centralwidget = QtWidgets.QWidget(SendWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(380, 450))
        self.centralwidget.setMaximumSize(QtCore.QSize(380, 450))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        self.R_plainTextEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.R_plainTextEdit.setObjectName("R_plainTextEdit")
        self.gridLayout.addWidget(self.R_plainTextEdit, 5, 0, 1, 1)
        self.R_titleLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.R_titleLabel.setFont(font)
        self.R_titleLabel.setObjectName("R_titleLabel")
        self.gridLayout.addWidget(self.R_titleLabel, 0, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.R_encryptedTextEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.R_encryptedTextEdit.setObjectName("R_encryptedTextEdit")
        self.gridLayout.addWidget(self.R_encryptedTextEdit, 10, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem1, 8, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem2, 11, 0, 1, 1)
        self.R_encryptedMessageLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.R_encryptedMessageLabel.setFont(font)
        self.R_encryptedMessageLabel.setObjectName("R_encryptedMessageLabel")
        self.gridLayout.addWidget(self.R_encryptedMessageLabel, 9, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.R_plainTextLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.R_plainTextLabel.setFont(font)
        self.R_plainTextLabel.setObjectName("R_plainTextLabel")
        self.gridLayout.addWidget(self.R_plainTextLabel, 4, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem3, 6, 0, 1, 1)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.R_sendButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.sendToSender())
        font = QtGui.QFont()
        font.setPointSize(12)
        self.R_sendButton.setFont(font)
        self.R_sendButton.setObjectName("R_sendButton")
        self.gridLayout_7.addWidget(self.R_sendButton, 0, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_7.addItem(spacerItem4, 1, 0, 1, 1)
        self.R_messagesTextEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.R_messagesTextEdit.setReadOnly(True)
        self.R_messagesTextEdit.setObjectName("R_messagesTextEdit")
        self.gridLayout_7.addWidget(self.R_messagesTextEdit, 3, 0, 1, 1)
        self.R_messagesLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.R_messagesLabel.setFont(font)
        self.R_messagesLabel.setObjectName("R_messagesLabel")
        self.gridLayout_7.addWidget(self.R_messagesLabel, 2, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_7.addItem(spacerItem5, 4, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_7, 12, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.R_encryptButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.cipher_encrypt())
        font = QtGui.QFont()
        font.setPointSize(12)
        self.R_encryptButton.setFont(font)
        self.R_encryptButton.setObjectName("R_encryptButton")
        self.horizontalLayout.addWidget(self.R_encryptButton)
        self.R_decryptButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.cipher_decrypt())
        font = QtGui.QFont()
        font.setPointSize(12)
        self.R_decryptButton.setFont(font)
        self.R_decryptButton.setObjectName("R_decryptButton")
        self.horizontalLayout.addWidget(self.R_decryptButton)
        self.gridLayout.addLayout(self.horizontalLayout, 7, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 2, 2)
        SendWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SendWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 380, 21))
        self.menubar.setObjectName("menubar")
        self.menuDQSS_Encrypted_Messenger = QtWidgets.QMenu(self.menubar)
        self.menuDQSS_Encrypted_Messenger.setObjectName("menuDQSS_Encrypted_Messenger")
        SendWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SendWindow)
        self.statusbar.setObjectName("statusbar")
        SendWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuDQSS_Encrypted_Messenger.menuAction())

        self.retranslateUi(SendWindow)
        QtCore.QMetaObject.connectSlotsByName(SendWindow)

    def retranslateUi(self, SendWindow):
        _translate = QtCore.QCoreApplication.translate
        SendWindow.setWindowTitle(_translate("SendWindow", "MainWindow"))
        self.R_titleLabel.setText(_translate("SendWindow", "DQSS Encrypted Messenger"))
        self.R_encryptedMessageLabel.setText(_translate("SendWindow", "Encrypted Text"))
        self.R_plainTextLabel.setText(_translate("SendWindow", "Plain Text"))
        self.R_sendButton.setText(_translate("SendWindow", "Send"))
        self.R_messagesLabel.setText(_translate("SendWindow", "Messages"))
        self.R_encryptButton.setText(_translate("SendWindow", "Encrypt"))
        self.R_decryptButton.setText(_translate("SendWindow", "Decrypt"))
        self.menuDQSS_Encrypted_Messenger.setTitle(_translate("SendWindow", "DQSS Encrypted Messenger 2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SendWindow = QtWidgets.QMainWindow()
    ui = Ui_SendWindow()
    ui.setupUi(SendWindow)
    SendWindow.show()
    sys.exit(app.exec())
