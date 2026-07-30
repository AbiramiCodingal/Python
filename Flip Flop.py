# palidrome
def palidrome(tuple1):
    s = 0
    e = len(tuple1)-1
    while s < e:
        print(e)    
        print(s)
        if tuple1[s] != tuple1[e]:
            return False
        s += 1
        e -= 1
    return True

tuple1 = (1,2,3,3,2,1)
if palidrome(tuple1):
    print("the give tuple is palidrome")
else:
    print("the given tuple is not palidrome")