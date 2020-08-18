from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import mysql.connector
import ICBM

class GUIClass():
    ### 쓰레드, http 공부
    def __init__(self, ui):
        Form.resize(680, 333)
        self.idx = 0
        self.checked = False
        self.window = ui

        self.window.registerButton.clicked.connect(self.moveRegisterPage)
        self.window.loginButton.clicked.connect(self.login)

        self.window.idDuplicationCheckButton.clicked.connect(self.idDuplicationCheck)
        self.window.registerConfirmButton.clicked.connect(self.register)
        self.window.registerCancelButton.clicked.connect(self.cancelRegister)

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
                self.setIdx(row[0])
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
            self.window.stackedWidget.setCurrentIndex(2)
            # 로그인 시 서버에 연결 필요?
        
    def setIdx(self, _idx): # 로그인된 회원의 idx값 받아오기
        self.idx = _idx
    def getIdx(self):
        return self.idx

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
    def printRoom(self, _id): # 현재 생성되어있는 방 리스트 gridLayout에 출력, id 받아와서 제목에 출력(이건 새로 함수 만들까 생각중)
        pass
    def movePage(self): # 방의 갯수가 10개를 넘어갈 경우 활성화, 화살표 버튼으로 이전 10개, 다음 10개 출력
        pass
    def enterRoom(self): # 생성된 방에 입장
        pass
    def moveMakeRoomPage(self): # 방 만들기 페이지로 이동
        pass

    ### makeRoomPage - 3
    def makeRoom(self): # 방 만들기 기능 구현, 제목을 받고, 비밀방인지 아닌지 받고, 비밀방이라면 PW창 활성화
        pass
    def cancelMakeRoom(self): # 방 만들기 취소, mainPage로 돌아감
        pass

    ### room - 4
    def setTitle(self): # 방 제목 받아와서 설정
        pass
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
