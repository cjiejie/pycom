import serial


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




