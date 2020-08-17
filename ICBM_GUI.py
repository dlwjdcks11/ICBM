from PyQt5 import QtCore, QtGui, QtWidgets
import ICBM

class GUIClass():
    ### 쓰레드, http 공부
    def __init__(self, ui):
        self.window = ui

    ### loginPage
    def moveRegisterPage(self): # 회원가입 페이지로 이동
        pass
    def login(self): # 아이디, 비밀번호 확인 후 로그인
        pass

    ### registerPage
    def idDuplicationCheck(self): # 아이디 중복확인
        pass
    def register(self): # 회원가입, DB update
        pass
    def cancelRegister(self): # 취소, 로그인화면으로 되돌아감, LineEdit 초기화
        pass
    
    ### mainPage
    def printRoom(self, _id): # 현재 생성되어있는 방 리스트 gridLayout에 출력, id 받아와서 제목에 출력(이건 새로 함수 만들까 생각중)
        pass
    def movePage(self): # 방의 갯수가 10개를 넘어갈 경우 활성화, 화살표 버튼으로 이전 10개, 다음 10개 출력
        pass
    def enterRoom(self): # 생성된 방에 입장
        pass
    def moveMakeRoomPage(self): # 방 만들기 페이지로 이동
        pass

    ### makeRoomPage
    def makeRoom(self): # 방 만들기 기능 구현, 제목을 받고, 비밀방인지 아닌지 받고, 비밀방이라면 PW창 활성화
        pass
    def cancelMakeRoom(self): # 방 만들기 취소, mainPage로 돌아감
        pass

    ### room
    def setTitle(self): # 방 제목 받아와서 설정
        pass
    def quitRoom(self): # 방 나가기
        pass
    def getMember(self): # 현재 방의 인원수와 이름을 전부 받아서 출력
        pass
    def chat(self): # 명령어, 채팅 등을 받아서 실행(버튼에 연결)
        pass
    def youtubeAPI(self): # youtube API를 이용, 영상 검색, 출력, 제목 받아오기 실행
        pass

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = ICBM.Ui_Form()
    ui.setupUi(Form)

    gc = GUIClass(ui)

    Form.show()
    sys.exit(app.exec_())
