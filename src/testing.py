import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from demo import Ui_Dialog


def start():
    app = QApplication(sys.argv)
    window = QWidget()
    window.show()
    window.setGeometry(100, 100, 500, 500)
    window.setWindowTitle("lel")
    window.setWindowIcon(QIcon("icons/lambda-icon.jpg"))

    sys.exit(app.exec_())

def testApp():
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    testApp()
    #start()
