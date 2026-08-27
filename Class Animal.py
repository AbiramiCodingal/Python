from abc import ABC,abstractmethod
        
class Animal(ABC):
    @abstractmethod
    def move(self):
        pass

class Human(Animal):
    def move(self):
        print("I can walk and move")

class Snake(Animal):
    def move(self):
        print("I move by slithering")

class Fish(Animal):
    def move(self):
        print("I move by swimming")

class Bird(Animal):
    def move(self):
        print("I move by flying")

h1 = Human()
h1.move()
s1 = Snake()
s1.move()
f1 = Fish()
f1.move()
b1 = Bird()
b1.move()