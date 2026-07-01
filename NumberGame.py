# NumberGame
import random
comp = random.randint(1,50)
i = 0
while i<= 5:
    user=int(input("enter a number : "))
    if user == comp:
        print("You got it!!")
        break
    elif user < comp:
        print("You are less")
    else:
        print("You are greater")