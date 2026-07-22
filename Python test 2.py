# Calculator

def add(a,b):
    return (a+b)
def sub(a,b):
    return (a-b)
def mul(a,b):
    return (a*b)
def div(a,b):
    return (a/b)
choose = int(input("enter a your choise,1 - add,2 - sub,3 - mul,4 - div"))
a = int(input("enter a number : "))
b = int(input("enter a number : "))
if choose == 1:
    print (add(a,b))
elif choose == 2:
    print (sub(a,b))
elif choose == 3:
    print (mul(a,b))
elif choose == 4:
    print (div(a,b))