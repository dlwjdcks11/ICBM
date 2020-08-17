from PyQt5 import QtCore, QtGui, QtWidgets
import ICBM

class GUIClass():
    def __init__(self, ui):
        self.window = ui

    def register(self):
        pass
    def login(self):
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
