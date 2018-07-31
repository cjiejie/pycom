from PyQt5 import QtCore, QtGui, QtWidgets
from mainwindow import MainWindow
import sys


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()

    mainWindow.ThreadStartUp()

    exit_flag = app.exec_()

    print("exit_flag:%d"%exit_flag)

    if not exit_flag:
        mainWindow.ThreadStop()
        print("system exit!")
        sys.exit()




