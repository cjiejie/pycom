from PyQt5 import QtCore, QtGui, QtWidgets
from ui_my import Ui_MainWindow
import sys
import serial.tools.list_ports

com_on_off = False
wifi_on_off = False

port_list = list(serial.tools.list_ports.comports())


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        global port_list
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.obj_get_data.setText("wait...")

        for item in port_list:
            self.obj_com_port.addItem(str(item))
        for item in ["9600", "38400", "115200"]:
            self.obj_com_baud.addItem(item)

        self.obj_com_on_off.clicked.connect(self.WindowComPower)
        self.obj_wifi_on_off.clicked.connect(self.WindowWifiPower)
        self.obj_recv_clear.clicked.connect(self.WindowClearRecv)
        self.obj_send_cmd.clicked.connect(self.WindowSendDataCmd)

        self.obj_sta.textChanged.connect(self.WindowStu)

    def WindowGetData(self):
        self.obj_get_data.setText("wait...2")

    def WindowSendData(self):
        self.obj_send_data.setText("...")

    def WindowComPower(self):
        global com_on_off
        print(com_on_off)
        if com_on_off:
            self.obj_com_on_off.setText("打开")
            com_on_off = False

        else :
            print("here is :", sys._getframe().f_lineno)
            self.obj_com_on_off.setText("关闭")
            com_on_off = True

    def WindowWifiPower(self):
        global wifi_on_off
        print(wifi_on_off)
        if wifi_on_off:
            self.obj_wifi_on_off.setText("打开")
            wifi_on_off = False

        else :
            print("here is :", sys._getframe().f_lineno)
            self.obj_wifi_on_off.setText("关闭")
            wifi_on_off = True

    def WindowClearRecv(self):
        self.obj_get_data.setText("")
        self.obj_send_data.setText("")
        print("here is :", sys._getframe().f_lineno)

    def WindowSendDataCmd(self):
        print("here is :", sys._getframe().f_lineno)


    def WindowStu(self,p_str):
        self.obj_sta.setText("OK")
