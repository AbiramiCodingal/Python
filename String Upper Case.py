# class uppercase
class iostring:
    def intro(self,str1):
        self.str1 = "";

    def get_string(self):
        self.str1 = input("enter the string : ")

    def put_string(self):
        print("The upper case is",self.str1.upper())

obj1 = iostring()
obj1.get_string()
obj1.put_string()