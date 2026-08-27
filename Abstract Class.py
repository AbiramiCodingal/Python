from abc import ABC,abstractmethod

class Absclass(ABC):

    def printx(self,x):
        print("The value is",x)

    @abstractmethod
    def task(self):
        print("I am from inherited class")

class inh(Absclass):
    def task(self):
        print("I am from inherited class")


obj1 = inh()
obj1.task()
obj1.printx(90)