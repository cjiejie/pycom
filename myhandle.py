import sys, time, datetime
import serial
import threading
from mainwindow import MainWindow as mw

class MyStruct:
    def __init__(self, name = ""):
        self.name = name
        self.data_dic = {}
        self.index = -1

    class Struct():
        def __init__(self, contents, name, message, status, num = -1):
            self.contents = contents
            self.name = name
            self.message = message
            self.status = status
            self.line_num = num

    def make_struct(self, contents, name, message, status, num = -1):
        return self.Struct(contents, name, message, status, num)


class ComClass:
    def __init__(self):
        self.name = 'parent'
        # 构造串口的属性
        self.fserial = None
        self.port = None
        self.baud = None
        self.com_power = False

    def ThreadStart(self):
        t1 = self.ReadDataThread(self)
        t2 = self.SendDataThread(self)
        t1.start()
        t2.start()

    def GetComPower(self):
        return self.com_power

    def OpenCom(self, port, baud):
        print("test")
        self.port = port
        self.baud = baud
        print("port:%s,baud:%s"%(self.port, self.baud))
        if len(self.port) <= 0:
            print("The Serial port can't find!")
            self.com_power = False
            return False
        try:
            self.fserial = serial.Serial(self.port, self.baud, timeout=60)
            print("The Serial port open OK!")
            print("com_power is :", self.com_power)
            self.com_power = True
            return True
        except:
            print("The Serial port open Fail!")
            self.com_power = False
            return False


    def CloseCom(self):
        print("Close Serial port!")
        print("com_power is :", self.com_power)
        self.fserial.close()
        self.com_power = False


    class ReadDataThread(threading.Thread):
        def __init__(self, parent):
            self.parent = parent
            threading.Thread.__init__(self)

        def run(self):
            self.name = "ReadData"
            print("here is ReadDataThread:", sys._getframe().f_lineno)

            while True:
                while self.parent.GetComPower():
                    try:
                        data = self.parent.fserial.readline()
                        if len(data) <= 0:
                            #10ms 读
                            time.sleep(0.01)
                            continue
                        else:
                            print("read0 ###########!")
                            mw.WindowGetData("123456789")
                            print("read1 ###########!")
                    except:
                        print("read err!")
                        time.sleep(5)
                time.sleep(0.05)

    class SendDataThread(threading.Thread):
        def __init__(self, name=""):
            threading.Thread.__init__(self)
            self.name = name

        def run(self):
            global fserial
            self.name = "ReadData"
            print("here is SendDataThread:", sys._getframe().f_lineno)

