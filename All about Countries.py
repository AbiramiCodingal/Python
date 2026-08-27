# polymorphoism

class India():
    def capital(self):
        print("New Delhi is the capital of India.")

    def language(self):
        print("The Widely spoken laguage in India is Hindi")

    def climate(self):
        print("The climate of India is hot")

class USA:
     
     def capital(self):
             print("Washington DC is the capital of USA.")
     
     def language(self):
             print("The Widely spoken laguage in USA is English")
     
     def climate(self):
             print("The climate of USA is cool")

obj1 = India()
obj2 = USA()

for obj in (obj1,obj2):
      obj.capital()
      obj.climate()
      obj.language()