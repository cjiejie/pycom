from PyQt5 import QtCore, QtGui, QtWidgets
from ui_my import Ui_MainWindow
import sys, time, datetime
import serial.tools.list_ports
import myhandle
import threading
import queue

com_on_off = False
wifi_on_off = False

port_list = list(serial.tools.list_ports.comports())


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        global port_list
        super(MainWindow, self).__init__(parent)
        self.que = queue.Queue(2048)
        self.handle = myhandle.ComClass()

        self.setupUi(self)

        self.obj_get_data.setText("wait...")
        self.obj_get_data.setMinimumHeight(100)

        for item in port_list:
            self.obj_com_port.addItem(str(item[0]))
        for item in ["19200", "9600", "38400", "115200"]:
            self.obj_com_baud.addItem(item)

        self.obj_com_on_off.clicked.connect(self.WindowComPower)
        self.obj_wifi_on_off.clicked.connect(self.WindowWifiPower)
        self.obj_recv_clear.clicked.connect(self.WindowClearRecv)
        self.obj_send_cmd.clicked.connect(self.WindowSendDataCmd)

    def ThreadStartUp(self):
        print("here is thread start:", sys._getframe().f_lineno)
        t1 = ReadDataThread(self.handle, self)
        t2 = SendDataThread(self.handle)
        t3 = ShowGetDataThread(self)
        t1.start()
        t2.start()
        t3.start()

    def WindowGetData(self, p_str):
        cursor = self.obj_get_data.textCursor()
        self.obj_get_data.setTextCursor(cursor)
        # for i in p_str:
        #     print('%#x' % ord(i))
        #     self.obj_get_data.append(i)
        self.obj_get_data.append(p_str.rstrip('\r\n'))

    def WindowSendData(self):
        self.obj_send_data.setText("...")

    def WindowComPower(self):
        global com_on_off
        print("here is :", sys._getframe().f_lineno)
        print(com_on_off,sys._getframe().f_lineno)
        if com_on_off:
            myhandle.ComClass.CloseCom(self.handle)
            self.obj_com_on_off.setText("打开")
            self.WindowStu("Serial closed!")
            com_on_off = False
        else:
            port = self.obj_com_port.currentText()
            baud = self.obj_com_baud.currentText()
            com_on_off = myhandle.ComClass.OpenCom(self.handle, port, baud)
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

    def WindowSendData(self, p_str):
        self.obj_send_data.setText(p_str)

    def WindowStu(self, p_str):
        self.obj_sta.setText(p_str)


class ReadDataThread(threading.Thread):
    def __init__(self, parent,parent_ui):
        self.parent = parent
        self.parent_ui = parent_ui
        threading.Thread.__init__(self)

    def run(self):
        self.name = "ReadData"
        print("here is ReadDataThread:", sys._getframe().f_lineno)
        while True:
            while self.parent.GetComPower():
                data = ''
                try:
                    while self.parent.fserial.inWaiting() > 0 and len(data) < 100:
                        try:
                            data += bytes.decode(self.parent.fserial.readline())
                        except:
                            data += bytes.decode(self.parent.fserial.read())
                except:
                    print("read except")
                    data = ''
                if len(data) > 0:
                    try:
                        print("read:%s"%data)
                        self.parent_ui.que.put(data)
                    except:
                        continue


class ShowGetDataThread(threading.Thread):
    def __init__(self, parent_ui):
        self.parent_ui = parent_ui
        threading.Thread.__init__(self)

    def run(self):
        print("here is ShowGetDataThread:", sys._getframe().f_lineno)
        while True:
            data = '123'
            # while self.parent_ui.que.empty() == False and len(data) < 100:
            #     data = data+self.parent_ui.que.get()
            if len(data) > 0:
                # print("here is ShowGetDataThread: %s"%data)
                self.parent_ui.WindowGetData(data)
                time.sleep(1)

class SendDataThread(threading.Thread):
    def __init__(self, name=""):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        global fserial
        self.name = "ReadData"
        print("here is SendDataThread:", sys._getframe().f_lineno)
