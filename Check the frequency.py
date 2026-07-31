# Count the frequency

dic1 = { "mouse":2,"cup":3,"coding":3,"test":2,"laptop":1,"lemon":2}
k = 2
count = 0
for key in dic1:
    if dic1[key] == k:
        count+=1

print(f"The number of keys having value {k} is {count}")