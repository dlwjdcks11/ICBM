from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QInputDialog, QWidget, QDialog
import mysql.connector, math
import ICBM

class GUIClass():
    ### 쓰레드, http 공부
    def __init__(self, ui):
        Form.resize(680, 333)
        self.id = ""
        self.roomTitle = ""
        self.pageNum = 0
        self.checked = False
        self.window = ui

        self.window.registerButton.clicked.connect(self.moveRegisterPage)
        self.window.loginButton.clicked.connect(self.login)

        self.window.idDuplicationCheckButton.clicked.connect(self.idDuplicationCheck)
        self.window.registerConfirmButton.clicked.connect(self.register)
        self.window.registerCancelButton.clicked.connect(self.cancelRegister)

        self.window.makeRoomButton.clicked.connect(self.moveMakeRoomPage)
        self.window.leftButton.clicked.connect(self.moveToLeft)
        self.window.rightButton.clicked.connect(self.moveToRight)

        self.window.roomPw.setEnabled(False)
        self.window.privateRoomCheck.stateChanged.connect(self.unEditable)
        self.window.roomConfirmButton.clicked.connect(self.makeRoom)
        self.window.roomCancelButton.clicked.connect(self.cancelMakeRoom)

    ### loginPage - 0
    def moveRegisterPage(self): # 회원가입 페이지로 이동
        self.window.stackedWidget.setCurrentIndex(1)
    def login(self): # 아이디, 비밀번호 확인 후 로그인
        self.id = self.window.idInput.text()
        self.pw = self.window.pwInput.text()
        self.sql = "SELECT * FROM member"
        cursor.execute(self.sql)

        for row in cursor.fetchall():
            self.idExist = False
            self.pwExist = False

            if self.id == row[1]:
                self.idExist = True
            if self.idExist and self.pw == row[2]:
                self.pwExist = True
                self.setId(row[1])
                break

        if not self.idExist:
            self.msg = QMessageBox()
            self.msg.setWindowTitle("id Error")
            self.msg.setText("아이디가 존재하지 않습니다.")
            self.msg.exec_()
        if self.idExist and not self.pwExist:
            self.msg = QMessageBox()
            self.msg.setWindowTitle("pw Error")
            self.msg.setText("비밀번호가 존재하지 않습니다.")
            self.msg.exec_()
        if self.idExist and self.pwExist:
            self.msg = QMessageBox()
            self.msg.setWindowTitle("correct")
            self.msg.setText("로그인 성공")
            self.msg.exec_()
            self.window.idInput.clear()
            self.window.pwInput.clear()
            Form.resize(1534, 973)
            self.setLobbyTitle()
            self.printRoom()
            self.window.stackedWidget.setCurrentIndex(2)
            # 로그인 시 서버에 연결 필요?
        
    def setId(self, _id): # 로그인된 회원의 idx값 받아오기
        self.id = _id
    def getId(self):
        return self.id

    ### registerPage - 1
    def idDuplicationCheck(self): # 아이디 중복확인
        self.registerId = self.window.registerIdInput.text()
        self.idExist = False
        self.sql = "SELECT id FROM member"
        cursor.execute(self.sql)

        for row in cursor.fetchall():
            if (row[0] == self.registerId):
                self.idExist = True
                break
        
        if self.idExist:
            self.msg = QMessageBox()
            self.msg.setWindowTitle("id Error")
            self.msg.setText("이미 존재하는 아이디입니다.")
            self.msg.exec_()
        else:
            self.setChecked(True)
            self.msg = QMessageBox()
            self.msg.setWindowTitle("id OK")
            self.msg.setText("사용 가능한 아이디입니다.")
            self.msg.exec_()
            
    def register(self): # 회원가입, DB update
        if not self.getChecked():
            self.msg = QMessageBox()
            self.msg.setWindowTitle("need check")
            self.msg.setText("아이디 중복체크를 해주세요.")
            self.msg.exec_()
        else:
            self.registerId = self.window.registerIdInput.text()
            self.registerPw = self.window.registerPwInput.text()
            self.sql = "INSERT INTO member(id, pw) VALUES(%s, %s)"
            cursor.execute(self.sql, (self.registerId, self.registerPw, ))
            con.commit()
            self.msg = QMessageBox()
            self.msg.setWindowTitle("register OK")
            self.msg.setText("회원가입 완료")
            self.msg.exec_()
            self.window.stackedWidget.setCurrentIndex(0)

    def cancelRegister(self): # 취소, 로그인화면으로 되돌아감, LineEdit 초기화
        self.window.registerIdInput.clear()
        self.window.registerPwInput.clear()
        self.window.stackedWidget.setCurrentIndex(0)

    def setChecked(self, _checked): # 중복확인 했으면 값 True
        self.checked = _checked
    def getChecked(self):
        return self.checked
    
    ### mainPage - 2
    def setLobbyTitle(self):
        self.window.clientName.setText(self.getId() + "님 안녕하세요.")
    def printRoom(self): # 현재 생성되어있는 방 리스트 gridLayout에 출력
        self.i = 0
        self.startNum = self.getPageNum() * 10
        self.sql = "SELECT * FROM room LIMIT %s, 10"
        cursor.execute(self.sql, (self.startNum, ))

        for row in cursor.fetchall():
            self.newNum = QtWidgets.QLabel((str)(self.i + self.startNum + 1))
            self.newLabel = QtWidgets.QLabel(row[1])
            self.newButton = QtWidgets.QPushButton('입장')
            self.newButton.clicked.connect(lambda state, idx=row[0]: self.enterRoom(idx))
            self.newNum.setStyleSheet("background-color: black;" "color: white;")
            self.newNum.setAlignment(QtCore.Qt.AlignCenter)
            self.newLabel.setStyleSheet("background-color: black;" "color: white;")
            self.newNum.setMaximumWidth(50)
            self.newButton.setMaximumWidth(90)
            self.newNum.setMinimumHeight(30)
            self.newLabel.setMinimumHeight(30)
            self.newButton.setMinimumHeight(30)
            self.window.roomList.addWidget(self.newNum, self.i, 0)
            self.window.roomList.addWidget(self.newLabel, self.i, 1)
            self.window.roomList.addWidget(self.newButton, self.i, 2)
            self.i += 1

    def moveToLeft(self):
        if self.getPageNum() == 0: # 페이지 왼쪽 끝
            return
        self.tmp = self.getPageNum()
        self.setPageNum(self.tmp - 1)
        self.printRoom()
    def moveToRight(self):
        if self.getPageNum() == (math.ceil(self.getPageNum()) // 10 - 1): # 페이지 오른쪽 끝
            return
        self.tmp = self.getPageNum()
        self.setPageNum(self.tmp + 1)
        self.printRoom()

    def enterRoom(self, _idx): # 생성된 방에 입장
        self.private = 0
        self.pw = 0
        self.sql = "SELECT * FROM room WHERE idx=%s"
        cursor.execute(self.sql, (_idx, ))

        for row in cursor.fetchall():
            self.setRoomTitle(row[1])
            self.private = row[2]
            self.pw = row[3]
        
        if self.private == 0:
            self.setTitle()
            self.window.stackedWidget.setCurrentIndex(4)
        else:
            while True:
                text, ok = QInputDialog.getInt(self, '비밀번호', '비밀번호를 입력하세요(숫자만)') # error why?
                print("did")
                if ok:
                    if self.pw != text:
                        self.msg = QMessageBox()
                        self.msg.setWindowTitle("pw Error")
                        self.msg.setText("비밀번호가 틀렸습니다.")
                        self.msg.exec_()
                    else:
                        self.setTitle()
                        self.window.stackedWidget.setCurrentIndex(4)
                        break
        
    def moveMakeRoomPage(self): # 방 만들기 페이지로 이동
        Form.resize(680, 333)
        self.window.stackedWidget.setCurrentIndex(3)
    def setPageNum(self, _pageNum):
        self.pageNum = _pageNum
    def getPageNum(self):
        return self.pageNum
    def setRoomTitle(self, _roomTitle):
        self.roomTitle = _roomTitle
    def getRoomTitle(self):
        return self.roomTitle

    ### makeRoomPage - 3
    def unEditable(self):
        if not self.window.privateRoomCheck.isChecked():
            self.window.roomPw.setEnabled(False)
        else:
            self.window.roomPw.setEnabled(True)
    def makeRoom(self): # 방 만들기 기능 구현, 제목을 받고, 비밀방인지 아닌지 받고, 비밀방이라면 PW창 활성화
        self.title = self.window.roomTitleInput.text()
        if self.window.privateRoomCheck.isChecked():
            self.pw = self.window.roomPw.text()
            self.sql = "INSERT INTO room(title, private, pw) VALUES(%s, %s, %s)"
            cursor.execute(self.sql, (self.title, 1, self.pw, ))
        else:
            self.sql = "INSERT INTO room(title, private) VALUES(%s, %s)"
            cursor.execute(self.sql, (self.title, 0, ))
        con.commit()
        Form.resize(1534, 973)
        self.setLobbyTitle()
        self.printRoom()
        self.window.stackedWidget.setCurrentIndex(2)
        # 서버 연결
    def cancelMakeRoom(self): # 방 만들기 취소, mainPage로 돌아감
        self.window.roomTitleInput.clear()
        self.window.privateRoomCheck.setChecked(False)
        self.window.roomPw.clear()
        Form.resize(1534, 973)
        self.setLobbyTitle()
        self.printRoom()
        self.window.stackedWidget.setCurrentIndex(2)

    ### room - 4
    def setTitle(self): # 방 제목 받아와서 설정
        self.window.roomTitle.setText(self.getRoomTitle())
    def quitRoom(self): # 방 나가기
        pass
    def getMember(self): # 현재 방의 인원수와 이름을 전부 받아서 출력
        pass
    def chat(self): # 명령어, 채팅 등을 받아서 넘김(버튼에 연결) - 클래스로 빼야하나
        pass
    def youtubeAPI(self): # youtube API를 이용, 영상 검색, 출력, 제목 받아오기 실행
        pass

if __name__ == "__main__":
    import sys

    config = {
        "user": "admin",
        "password": "1234",
        "host": "127.0.0.1",
        "database": "ICBM",
        "port": "3306"
    }
    con = mysql.connector.connect(**config)
    cursor = con.cursor()
    
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = ICBM.Ui_Form()
    ui.setupUi(Form)

    gc = GUIClass(ui)

    Form.show()
    sys.exit(app.exec_())
