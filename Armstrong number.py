# Armstrong number

n = int(input("enter the number : "))

t = n 
s = 0
while t > 0:
    r = t%10
    s = s + r ** 3
    t //= 10

if s == n:
    print(n, "is an armstrong number ")
else:
    print(n, "is not an armstrong number ")
