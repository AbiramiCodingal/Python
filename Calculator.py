# Calculator
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

a = int(input("enter first number : "))
b = int(input("enter second number : "))
choice = input("\n1.Addition \n2.Subtraction \n3.Multiplication \n4.Division \nEnter yourchoice(1-4)")
if choice == "1":
    print(a,"+",b,"=",add(a,b))
elif choice == "2":
    print(a,"-",b,"=",sub(a,b))
elif choice == "3":
    print(a,"*",b,"=",mul(a,b))
elif choice == "4":
    print(a,"/",b,"=",div(a,b))
else:
    print("Invalid input")

