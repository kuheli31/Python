#rock paper scissors game
# 0=rock
# 1=paper
# 2=scissors

import random

list1 = ['rock', 'paper', 'scissors']

userChoice = input("Enter your choice: rock, paper, scissors: ")
computerChoice=random.choice(list1)
print("Computer choice: ", computerChoice)

if userChoice == computerChoice:
    print("It's a tie!")
elif userChoice == 'rock':  
    if computerChoice == 'scissors':
        print("You win!")
    else:
        print("You lose!")
elif userChoice == 'paper':
    if computerChoice == 'rock':
        print("You win!")
    else:
        print("You lose!")
elif userChoice == 'scissors':
    if computerChoice == 'paper':
        print("You win!")
    else:
        print("You lose!")
else:
    print("Invalid input! You have not entered rock, paper or scissors, try again.")
