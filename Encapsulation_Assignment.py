class employee:
    def __init__(self, sal):
        self._sal=20

class employee:
    def __init__(self, name):
        self.__name=name

class employee:
    def __init__(self, name):
        self.__name = name 

    def getPrivate(self):
        print(self.__name)

    def setPrivate(self, private):
        self.__name = private


obj = employee(20)
obj._sal = 40
print(obj._sal)


obj = employee("al")
obj.getPrivate()
obj.setPrivate("bill")
obj.getPrivate()
