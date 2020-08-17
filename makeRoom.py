# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'makeRoom.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(680, 333)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 10, 351, 81))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(30, 100, 621, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 130, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.roomTitleInput = QtWidgets.QLineEdit(Form)
        self.roomTitleInput.setGeometry(QtCore.QRect(160, 130, 481, 31))
        self.roomTitleInput.setObjectName("roomTitleInput")
        self.privateRoomCheck = QtWidgets.QCheckBox(Form)
        self.privateRoomCheck.setGeometry(QtCore.QRect(40, 180, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(11)
        self.privateRoomCheck.setFont(font)
        self.privateRoomCheck.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.privateRoomCheck.setObjectName("privateRoomCheck")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 220, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.roomPw = QtWidgets.QLineEdit(Form)
        self.roomPw.setGeometry(QtCore.QRect(220, 220, 421, 31))
        self.roomPw.setObjectName("roomPw")
        self.roomCancelButton = QtWidgets.QPushButton(Form)
        self.roomCancelButton.setGeometry(QtCore.QRect(400, 270, 112, 34))
        self.roomCancelButton.setObjectName("roomCancelButton")
        self.roomConfirmButton = QtWidgets.QPushButton(Form)
        self.roomConfirmButton.setGeometry(QtCore.QRect(530, 270, 112, 34))
        self.roomConfirmButton.setObjectName("roomConfirmButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Room Settings"))
        self.label_2.setText(_translate("Form", "방 제목"))
        self.privateRoomCheck.setText(_translate("Form", "비밀방 설정"))
        self.label_3.setText(_translate("Form", "비밀번호(숫자만)"))
        self.roomCancelButton.setText(_translate("Form", "취소"))
        self.roomConfirmButton.setText(_translate("Form", "만들기"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

