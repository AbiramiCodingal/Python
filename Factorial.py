def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

n = int(input("enter the number :"))
print("the factorial of the number is ",fact(n))