# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
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
        self.label.setGeometry(QtCore.QRect(30, 20, 261, 81))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(30, 120, 621, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.idInput = QtWidgets.QLineEdit(Form)
        self.idInput.setGeometry(QtCore.QRect(100, 160, 431, 31))
        self.idInput.setObjectName("idInput")
        self.pwInput = QtWidgets.QLineEdit(Form)
        self.pwInput.setGeometry(QtCore.QRect(100, 220, 431, 31))
        self.pwInput.setObjectName("pwInput")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 150, 31, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 210, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.idDuplicationCheckButton = QtWidgets.QPushButton(Form)
        self.idDuplicationCheckButton.setGeometry(QtCore.QRect(540, 160, 112, 34))
        self.idDuplicationCheckButton.setObjectName("idDuplicationCheckButton")
        self.cancelButton = QtWidgets.QPushButton(Form)
        self.cancelButton.setGeometry(QtCore.QRect(290, 270, 112, 34))
        self.cancelButton.setObjectName("cancelButton")
        self.checkButton = QtWidgets.QPushButton(Form)
        self.checkButton.setGeometry(QtCore.QRect(420, 270, 112, 34))
        self.checkButton.setObjectName("checkButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Register"))
        self.label_2.setText(_translate("Form", "ID"))
        self.label_3.setText(_translate("Form", "PW"))
        self.idDuplicationCheckButton.setText(_translate("Form", "중복확인"))
        self.cancelButton.setText(_translate("Form", "취소"))
        self.checkButton.setText(_translate("Form", "등록"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

