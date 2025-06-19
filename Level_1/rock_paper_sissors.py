# This is the rock paper sissor game

from random import randint
components = ["rock", "paper", "scissors"]

component_index = randint(0,2)
component = components[component_index]

user_input = int(input("Enter 1 for rock 2 for paper 3 for scissors : ")) # By default the input() return a string

if component == 'rock':
    if user_input == 1:
        print("Draw")
    elif user_input == 2:
        print("You Win!")
    elif user_input == 3:
        print("Computer Wins")
elif component == 'paper':
    if user_input == 1:
        print("You Lose!")
    elif user_input == 2:
        print("Draw!")
    elif user_input == 3:
        print("You Win")
elif component == 'scissors':
    if user_input == 1:
        print("You win!")
    elif user_input == 2:
        print("You Lose!")
    elif user_input == 3:
        print("Draw")

print(f"Computer choice was {component}")
