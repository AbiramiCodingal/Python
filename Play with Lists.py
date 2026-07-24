# sum and average

list1 = [2,45,56,67,89]
sum = 0
for i in list1:
    sum+=i

print("the sum of the list is ",sum)
avg = sum/len(list1)
print("The average of the list is ",avg)

list1.sort()
print(list1)
print("the smallest is ",list1[0])
print("the largest is ",list1[len(list1)-1])