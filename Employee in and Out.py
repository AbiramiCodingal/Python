# consturctor

class employee:
    def __init__(self):
        print("employee created")

    def _del_(self):
        print("employee deleted")

def createobj():
    print("The employee is going to create")
    obj = employee()
    return obj

obj = createobj()
print("The emlpoyee is deleted")
del obj