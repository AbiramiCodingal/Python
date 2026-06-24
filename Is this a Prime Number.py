# Genrate Prime Number
l = int(input("enter the lower limit : ")) 
u = int(input("Enter the upper limit : ")) 
for i in range(l,u+1):
    for j in range(2,l):
        if i % j == 0:
            break
    else:
        print(i)