# Multiple exceptions
try:
    a,b = eval(input("enter the numbers separated by commas"))
    s = a/b
    print("the answer is ",s)
except SyntaxError:
    print("you have missed a comma")
except ZeroDivisionError:
    print("Number cannot be divided by zero")
except :
    print("an error occured")
finally:
    print("I will be there always")
