# computer price

class computer:
    def __init__(self):
       self.__maxprice = 1000

    def printmax(self):
        print("The max price of the computer is",self.__maxprice)

    def setmax(self,price):
        self.__maxprice = price

c1 = computer()
c1.__maxprice = 1400
c1.printmax()
c1.setmax(1900)
c1.printmax()