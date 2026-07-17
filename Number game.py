# numbergame
import random

computer =  random.randint(10,20)
while True:
    no = int(input("enter the number between 10 to 20 "))
    if no == computer:
        print("You win the game")
        break;
    elif no > computer:
        print("Your number is greater")
    else:
        print("Your number is lesser")