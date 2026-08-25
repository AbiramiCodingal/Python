#  creat a snack  boxes using sets
from array import array


box1 = {"Chips", "Biscuit", "Juice"}
box2 = {"Juice", "Chocolate", "Cake"}

print("Snack Box 1:", box1)
print("Snack Box 2:", box2)



box1.add("Sandwich")
print("\nAfter adding a new snack:")
print(box1)


common_snack = box1.intersection(box2)
print("\nCommon Snack:", common_snack)



snack_count = array('i', [10, 15, 20])

print("\nSnack Counts:")
print(snack_count)



snack_count.append(15)
print("\nAfter adding a new count:")
print(snack_count)



print("\nCount of 15:", snack_count.count(15))



snack_count.reverse()
print("\nReversed Snack Counts:")
print(snack_count)