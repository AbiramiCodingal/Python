# Value error
try:
    a = int(input("enter the number :"))
    print(a)
except ValueError as ex:
    print("an exception occured",ex)




