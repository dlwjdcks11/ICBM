# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'room.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1534, 973)
        self.roomTitle = QtWidgets.QLabel(Form)
        self.roomTitle.setGeometry(QtCore.QRect(30, 10, 231, 81))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(28)
        self.roomTitle.setFont(font)
        self.roomTitle.setObjectName("roomTitle")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(30, 110, 1461, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.quitButton = QtWidgets.QPushButton(Form)
        self.quitButton.setGeometry(QtCore.QRect(1350, 40, 121, 41))
        self.quitButton.setObjectName("quitButton")
        self.memberList = QtWidgets.QListWidget(Form)
        self.memberList.setGeometry(QtCore.QRect(50, 190, 351, 751))
        self.memberList.setObjectName("memberList")
        self.memberLabel = QtWidgets.QLabel(Form)
        self.memberLabel.setGeometry(QtCore.QRect(50, 150, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(12)
        self.memberLabel.setFont(font)
        self.memberLabel.setObjectName("memberLabel")
        self.chatInput = QtWidgets.QLineEdit(Form)
        self.chatInput.setGeometry(QtCore.QRect(420, 900, 941, 41))
        self.chatInput.setObjectName("chatInput")
        self.submitButton = QtWidgets.QPushButton(Form)
        self.submitButton.setGeometry(QtCore.QRect(1380, 900, 112, 41))
        self.submitButton.setObjectName("submitButton")
        self.chatList = QtWidgets.QListWidget(Form)
        self.chatList.setGeometry(QtCore.QRect(420, 190, 1071, 691))
        self.chatList.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.chatList.setObjectName("chatList")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(420, 150, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(530, 160, 111, 18))
        self.label_2.setObjectName("label_2")
        self.musicTitle = QtWidgets.QLabel(Form)
        self.musicTitle.setGeometry(QtCore.QRect(640, 160, 731, 18))
        self.musicTitle.setObjectName("musicTitle")
        self.youtubeThumbnail = QtWidgets.QWidget(Form)
        self.youtubeThumbnail.setGeometry(QtCore.QRect(1390, 130, 91, 51))
        self.youtubeThumbnail.setStyleSheet("background-color: black;\n"
"color: white;")
        self.youtubeThumbnail.setObjectName("youtubeThumbnail")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.roomTitle.setText(_translate("Form", "(방 제목)"))
        self.quitButton.setText(_translate("Form", "나가기"))
        self.memberLabel.setText(_translate("Form", "현재 인원 n명"))
        self.chatInput.setPlaceholderText(_translate("Form", "명령어 or 채팅 입력"))
        self.submitButton.setText(_translate("Form", "전송"))
        self.label.setText(_translate("Form", "Chatting"))
        self.label_2.setText(_translate("Form", "Now Playing: "))
        self.musicTitle.setText(_translate("Form", "(유튜브 제목)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

