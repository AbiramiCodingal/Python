#skip number 5
print("the number from 10 to 1 skips 5")
for i in range(10,0,-1):
    if i == 5:
        continue
    print(i)