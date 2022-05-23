class SI():
    def __init__(self):
        self.principal = int(input("enter principal: "))
        self.rate = int(input("enter rate: "))
        self.time = int(input("enter time: "))
    def mySI(self):
        self.mySI = (self.principal*self.rate*self.time)/100
        print("simple interest", self.mySI)

m = SI()
m.mySI()


