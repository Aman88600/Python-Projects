# This is the number guessing Game

# To generate the random number we must use the random module and use the randint() function
from random import randint

magic_number = randint(1,100)

attempts = 5

while attempts > 0:
    user_input = int(input("Enter Your Number : "))
    if user_input == magic_number:
        print("You Win!")
        break
    elif user_input > magic_number:
        print("Too High")
    elif user_input < magic_number:
        print("Too Low!")
    print(f"You Have {attempts} attempts Left")
    attempts -= 1

if attempts == 0:
    print(f"You Lose! magic number was {magic_number}")