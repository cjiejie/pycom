from PyQt5 import QtCore, QtGui, QtWidgets
from ui_my import Ui_MainWindow
import sys
import serial.tools.list_ports
import myhandle
import threading

com_on_off = False
wifi_on_off = False

port_list = list(serial.tools.list_ports.comports())


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        global port_list
        super(MainWindow, self).__init__(parent)

        self.handle = myhandle.ComClass()

        self.setupUi(self)
        # self.obj_get_data.setMaximumBlockCount(100)
        self.obj_get_data.setText("wait...")

        for item in port_list:
            self.obj_com_port.addItem(str(item[0]))
        for item in ["9600", "38400", "115200"]:
            self.obj_com_baud.addItem(item)

        self.obj_com_on_off.clicked.connect(self.WindowComPower)
        self.obj_wifi_on_off.clicked.connect(self.WindowWifiPower)
        self.obj_recv_clear.clicked.connect(self.WindowClearRecv)
        self.obj_send_cmd.clicked.connect(self.WindowSendDataCmd)

    def ThreadStartUp(self):
        self.handle.ThreadStart()

    def WindowGetData(self,str):
        self.obj_get_data.append(str)

    def WindowSendData(self):
        self.obj_send_data.setText("...")

    def WindowComPower(self):
        global com_on_off
        print(com_on_off,sys._getframe().f_lineno)
        if com_on_off:
            myhandle.ComClass.CloseCom(self.handle)
            print("here is :", sys._getframe().f_lineno)
            self.obj_com_on_off.setText("打开")
            self.WindowStu("Serial closed!")
            com_on_off = False
        else:
            port = self.obj_com_port.currentText()
            baud = self.obj_com_baud.currentText()
            print("here is :", sys._getframe().f_lineno)
            com_on_off = myhandle.ComClass.OpenCom(self.handle, port, baud)
            print("here is :", sys._getframe().f_lineno)
            print(com_on_off, sys._getframe().f_lineno)
            if com_on_off:
                self.obj_com_on_off.setText("关闭")
                self.WindowStu("Open Serial OK!")
                com_on_off = True
            else:
                self.obj_com_on_off.setText("打开")
                self.WindowStu("Open Serial Fail!")
                com_on_off = False

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

    def WindowGetData(self, p_str):
        self.obj_get_data.setText(p_str)

    def WindowSendData(self, p_str):
        self.obj_send_data.setText(p_str)

    def WindowStu(self, p_str):
        self.obj_sta.setText(p_str)

