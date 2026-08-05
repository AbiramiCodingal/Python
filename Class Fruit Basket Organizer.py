# Class Fruit Basket Organizer
     
basket1 = {"apple", "banana", "mango", "apple", "grape"}
basket2 = {"mango","kiwi", "banana", "kiwi"}
print("Basket 1:", basket1)
print("Basket 2:", basket2)

basket1.add("orange")
print("Basket 1 after adding orange:", basket1)

common_fruits = basket1.intersection(basket2)
print("Fruits in both baskets:", common_fruits)

import array as arr
fruit_counts = arr.array('i', [3,5,2,4])
print("Fruits counts array:", fruit_counts)

fruit_counts.insert(0,1)
fruit_counts.append(6)
print("Fruit counts after adding items",fruit_counts)

fruit_counts.reverse()
print("Reversed fruit counts array:", fruit_counts)


print("")
print("===== CLASS FRUIT BASKET ORGANISER =====")
print("Basket  1:", basket1)
print("Basket  2:", basket2)
print("shared fruits:", common_fruits)
print("Fruit counts:", fruit_counts)
print("=================================================")