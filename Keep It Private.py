# Private method
class myclass:
    __privvar = 28

    def __privmeth(self):
        print("I am private method")

    def publimeth(self):
            print("The value is",self.__privvar)

obj1 = myclass()
#print("the value of private variable is",obj1.__privvar)
#obj1.__privmeth()
obj1.publimeth()