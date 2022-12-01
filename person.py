class Person:
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return str(self.name)
    def getName(self):
        return self.name
    def setName(self,name):
        self.name = name