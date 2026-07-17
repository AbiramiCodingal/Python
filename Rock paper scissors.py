# Rock paper scissors
import random
choice = ['rock','paper','scissors']
while True:
    computer = random.choice(choice)
    user = input("enter rock or paper or scissors ")
    if computer == user:
        print("it is a tie")
    elif(user == 'rock' and computer == 'scissors') or (user == 'paper' and computer == 'rock') or (user == 'scissors' and computer == 'paper'):
        print("you win the game 😊")
    else:
        print("computer wins the game ☹️")
    print(computer)
    ch = input("do you want to play again (y / n) : ")
    if ch.lower() == 'n':
        break