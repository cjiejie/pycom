from PyQt5 import QtCore, QtGui, QtWidgets
from mainwindow import MainWindow
import sys


tmp_str = "OK"

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()

    mainWindow.ThreadStartUp()

    sys.exit(app.exec_())


