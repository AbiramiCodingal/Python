class FamilyMember:
    def __init__(self, eyecolor, height):
        self.eyecolor = eyecolor
        self.height = height

    def show_traits(self):
        print("The eye color is",self.eyecolor)
        print("The height is",self.height)

class kid(FamilyMember):
    def __init__(self, name, age, eyecolor, height):
        self.name = name
        self.age = age
        super().__init__(eyecolor, height)

    def show_traits(self):
        print("The name is", self.name)
        print("the age",self.age)
        super().show_traits()

    def favourite_hobby(self,hobby):
        print("the favourite hobby is",hobby)

child = kid("Maya",12,"brown","135cm")
child.show_traits()

child.favourite_hobby("Gardening")

print("Is this the subclass", issubclass(kid,FamilyMember))