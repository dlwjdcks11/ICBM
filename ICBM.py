# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ICBM.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1534, 973)
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1534, 973))
        self.stackedWidget.setStyleSheet("background-color: white;")
        self.stackedWidget.setObjectName("stackedWidget")
        self.loginPage = QtWidgets.QWidget()
        self.loginPage.setObjectName("loginPage")
        self.idInput = QtWidgets.QLineEdit(self.loginPage)
        self.idInput.setGeometry(QtCore.QRect(100, 150, 431, 31))
        self.idInput.setObjectName("idInput")
        self.pwInput = QtWidgets.QLineEdit(self.loginPage)
        self.pwInput.setGeometry(QtCore.QRect(100, 210, 431, 31))
        self.pwInput.setObjectName("pwInput")
        self.line = QtWidgets.QFrame(self.loginPage)
        self.line.setGeometry(QtCore.QRect(30, 110, 621, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.registerButton = QtWidgets.QPushButton(self.loginPage)
        self.registerButton.setGeometry(QtCore.QRect(290, 260, 112, 34))
        self.registerButton.setObjectName("registerButton")
        self.label_3 = QtWidgets.QLabel(self.loginPage)
        self.label_3.setGeometry(QtCore.QRect(40, 200, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.loginPage)
        self.label_2.setGeometry(QtCore.QRect(40, 140, 31, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.loginPage)
        self.label.setGeometry(QtCore.QRect(30, 20, 381, 81))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.loginButton = QtWidgets.QPushButton(self.loginPage)
        self.loginButton.setGeometry(QtCore.QRect(420, 260, 112, 34))
        self.loginButton.setObjectName("loginButton")
        self.stackedWidget.addWidget(self.loginPage)
        self.registerPage = QtWidgets.QWidget()
        self.registerPage.setObjectName("registerPage")
        self.pwInput_2 = QtWidgets.QLineEdit(self.registerPage)
        self.pwInput_2.setGeometry(QtCore.QRect(100, 220, 431, 31))
        self.pwInput_2.setObjectName("pwInput_2")
        self.line_2 = QtWidgets.QFrame(self.registerPage)
        self.line_2.setGeometry(QtCore.QRect(30, 120, 621, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_4 = QtWidgets.QLabel(self.registerPage)
        self.label_4.setGeometry(QtCore.QRect(40, 210, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.registerCancelButton = QtWidgets.QPushButton(self.registerPage)
        self.registerCancelButton.setGeometry(QtCore.QRect(290, 270, 112, 34))
        self.registerCancelButton.setObjectName("registerCancelButton")
        self.idInput_2 = QtWidgets.QLineEdit(self.registerPage)
        self.idInput_2.setGeometry(QtCore.QRect(100, 160, 431, 31))
        self.idInput_2.setObjectName("idInput_2")
        self.label_5 = QtWidgets.QLabel(self.registerPage)
        self.label_5.setGeometry(QtCore.QRect(40, 150, 31, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.registerPage)
        self.label_6.setGeometry(QtCore.QRect(30, 20, 261, 81))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(28)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.idDuplicationCheckButton = QtWidgets.QPushButton(self.registerPage)
        self.idDuplicationCheckButton.setGeometry(QtCore.QRect(540, 160, 112, 34))
        self.idDuplicationCheckButton.setObjectName("idDuplicationCheckButton")
        self.registerConfirmButton = QtWidgets.QPushButton(self.registerPage)
        self.registerConfirmButton.setGeometry(QtCore.QRect(420, 270, 112, 34))
        self.registerConfirmButton.setObjectName("registerConfirmButton")
        self.stackedWidget.addWidget(self.registerPage)
        self.mainPage = QtWidgets.QWidget()
        self.mainPage.setObjectName("mainPage")
        self.label_7 = QtWidgets.QLabel(self.mainPage)
        self.label_7.setGeometry(QtCore.QRect(40, 20, 161, 81))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(28)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.leftButton = QtWidgets.QPushButton(self.mainPage)
        self.leftButton.setGeometry(QtCore.QRect(710, 920, 41, 34))
        self.leftButton.setObjectName("leftButton")
        self.makeRoomButton = QtWidgets.QPushButton(self.mainPage)
        self.makeRoomButton.setGeometry(QtCore.QRect(1320, 40, 171, 51))
        self.makeRoomButton.setStyleSheet("")
        self.makeRoomButton.setObjectName("makeRoomButton")
        self.gridLayoutWidget = QtWidgets.QWidget(self.mainPage)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(50, 130, 1441, 771))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.roomList = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.roomList.setContentsMargins(0, 0, 0, 0)
        self.roomList.setObjectName("roomList")
        self.clientName = QtWidgets.QLabel(self.mainPage)
        self.clientName.setGeometry(QtCore.QRect(1000, 50, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.clientName.setFont(font)
        self.clientName.setObjectName("clientName")
        self.line_3 = QtWidgets.QFrame(self.mainPage)
        self.line_3.setGeometry(QtCore.QRect(40, 110, 1461, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.rightButton = QtWidgets.QPushButton(self.mainPage)
        self.rightButton.setGeometry(QtCore.QRect(770, 920, 41, 34))
        self.rightButton.setObjectName("rightButton")
        self.stackedWidget.addWidget(self.mainPage)
        self.makeRoomPage = QtWidgets.QWidget()
        self.makeRoomPage.setObjectName("makeRoomPage")
        self.roomPw = QtWidgets.QLineEdit(self.makeRoomPage)
        self.roomPw.setGeometry(QtCore.QRect(220, 230, 421, 31))
        self.roomPw.setObjectName("roomPw")
        self.line_4 = QtWidgets.QFrame(self.makeRoomPage)
        self.line_4.setGeometry(QtCore.QRect(30, 110, 621, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_8 = QtWidgets.QLabel(self.makeRoomPage)
        self.label_8.setGeometry(QtCore.QRect(40, 230, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.roomCancelButton = QtWidgets.QPushButton(self.makeRoomPage)
        self.roomCancelButton.setGeometry(QtCore.QRect(400, 280, 112, 34))
        self.roomCancelButton.setObjectName("roomCancelButton")
        self.roomTitleInput = QtWidgets.QLineEdit(self.makeRoomPage)
        self.roomTitleInput.setGeometry(QtCore.QRect(160, 140, 481, 31))
        self.roomTitleInput.setObjectName("roomTitleInput")
        self.label_9 = QtWidgets.QLabel(self.makeRoomPage)
        self.label_9.setGeometry(QtCore.QRect(30, 20, 351, 81))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(26)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.makeRoomPage)
        self.label_10.setGeometry(QtCore.QRect(40, 140, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(16)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.roomConfirmButton = QtWidgets.QPushButton(self.makeRoomPage)
        self.roomConfirmButton.setGeometry(QtCore.QRect(530, 280, 112, 34))
        self.roomConfirmButton.setObjectName("roomConfirmButton")
        self.privateRoomCheck = QtWidgets.QCheckBox(self.makeRoomPage)
        self.privateRoomCheck.setGeometry(QtCore.QRect(40, 190, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(11)
        self.privateRoomCheck.setFont(font)
        self.privateRoomCheck.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.privateRoomCheck.setObjectName("privateRoomCheck")
        self.stackedWidget.addWidget(self.makeRoomPage)
        self.roomPage = QtWidgets.QWidget()
        self.roomPage.setObjectName("roomPage")
        self.memberList = QtWidgets.QListWidget(self.roomPage)
        self.memberList.setGeometry(QtCore.QRect(50, 200, 351, 751))
        self.memberList.setObjectName("memberList")
        self.label_11 = QtWidgets.QLabel(self.roomPage)
        self.label_11.setGeometry(QtCore.QRect(530, 170, 111, 18))
        self.label_11.setObjectName("label_11")
        self.roomTitle = QtWidgets.QLabel(self.roomPage)
        self.roomTitle.setGeometry(QtCore.QRect(30, 20, 231, 81))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(28)
        self.roomTitle.setFont(font)
        self.roomTitle.setObjectName("roomTitle")
        self.chatInput = QtWidgets.QLineEdit(self.roomPage)
        self.chatInput.setGeometry(QtCore.QRect(420, 910, 941, 41))
        self.chatInput.setObjectName("chatInput")
        self.label_12 = QtWidgets.QLabel(self.roomPage)
        self.label_12.setGeometry(QtCore.QRect(420, 160, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.musicTitle = QtWidgets.QLabel(self.roomPage)
        self.musicTitle.setGeometry(QtCore.QRect(640, 170, 731, 18))
        self.musicTitle.setObjectName("musicTitle")
        self.memberLabel = QtWidgets.QLabel(self.roomPage)
        self.memberLabel.setGeometry(QtCore.QRect(50, 160, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(12)
        self.memberLabel.setFont(font)
        self.memberLabel.setObjectName("memberLabel")
        self.chatList = QtWidgets.QListWidget(self.roomPage)
        self.chatList.setGeometry(QtCore.QRect(420, 200, 1071, 691))
        self.chatList.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.chatList.setObjectName("chatList")
        self.youtubeThumbnail = QtWidgets.QWidget(self.roomPage)
        self.youtubeThumbnail.setGeometry(QtCore.QRect(1390, 140, 91, 51))
        self.youtubeThumbnail.setStyleSheet("background-color: black;\n"
"color: white;")
        self.youtubeThumbnail.setObjectName("youtubeThumbnail")
        self.submitButton = QtWidgets.QPushButton(self.roomPage)
        self.submitButton.setGeometry(QtCore.QRect(1380, 910, 112, 41))
        self.submitButton.setObjectName("submitButton")
        self.quitButton = QtWidgets.QPushButton(self.roomPage)
        self.quitButton.setGeometry(QtCore.QRect(1350, 50, 121, 41))
        self.quitButton.setObjectName("quitButton")
        self.line_5 = QtWidgets.QFrame(self.roomPage)
        self.line_5.setGeometry(QtCore.QRect(30, 120, 1461, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.stackedWidget.addWidget(self.roomPage)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.registerButton.setText(_translate("Form", "회원가입"))
        self.label_3.setText(_translate("Form", "PW"))
        self.label_2.setText(_translate("Form", "ID"))
        self.label.setText(_translate("Form", "Youtube Player"))
        self.loginButton.setText(_translate("Form", "로그인"))
        self.label_4.setText(_translate("Form", "PW"))
        self.registerCancelButton.setText(_translate("Form", "취소"))
        self.label_5.setText(_translate("Form", "ID"))
        self.label_6.setText(_translate("Form", "Register"))
        self.idDuplicationCheckButton.setText(_translate("Form", "중복확인"))
        self.registerConfirmButton.setText(_translate("Form", "등록"))
        self.label_7.setText(_translate("Form", "Lobby"))
        self.leftButton.setText(_translate("Form", "<"))
        self.makeRoomButton.setText(_translate("Form", "방 만들기"))
        self.clientName.setText(_translate("Form", "(사용자 이름)님 안녕하세요."))
        self.rightButton.setText(_translate("Form", ">"))
        self.label_8.setText(_translate("Form", "비밀번호(숫자만)"))
        self.roomCancelButton.setText(_translate("Form", "취소"))
        self.label_9.setText(_translate("Form", "Room Settings"))
        self.label_10.setText(_translate("Form", "방 제목"))
        self.roomConfirmButton.setText(_translate("Form", "만들기"))
        self.privateRoomCheck.setText(_translate("Form", "비밀방 설정"))
        self.label_11.setText(_translate("Form", "Now Playing: "))
        self.roomTitle.setText(_translate("Form", "(방 제목)"))
        self.chatInput.setPlaceholderText(_translate("Form", "명령어 or 채팅 입력"))
        self.label_12.setText(_translate("Form", "Chatting"))
        self.musicTitle.setText(_translate("Form", "(유튜브 제목)"))
        self.memberLabel.setText(_translate("Form", "현재 인원 n명"))
        self.submitButton.setText(_translate("Form", "전송"))
        self.quitButton.setText(_translate("Form", "나가기"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

