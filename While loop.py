# Armstrong number

n = int(input("enter the number : "))

t = n 
s = 0
while t > 0:
    r = t%10
    s = s +1
    t //= 10

print(s)