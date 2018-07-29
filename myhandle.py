import sys

globals()

class MyClass():
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
    #return struct item.
    def make_struct(self, contents, name, message, status, num = -1):
        return self.Struct(contents, name, message, status, num)
