# Diamond Pattern
n = int(input("enter the no. of rows : "))
space = 25
for i in range(1,n+1,2):
    for k in range(space):
        print(" ",end="")
    for j in range(1,i+1):
        print(j,end="")
    space-=1
    print()
space+=2
for i in range(n-2,0,-2):
    for k in range(space):
        print(" ",end="")
    for j in range(1,i+1):
        print(j,end="")
    space+=1
    print()