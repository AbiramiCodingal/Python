# Cube of the cube
def cube(x):
    return x*x*x

def divisible_by_three(x):
    if x%3 == 0:
        return cube(x)
    else:
        return False
    
n = int(input("enter the number :"))

print("The cube of the it is divisible by 3 -",divisible_by_three(n))