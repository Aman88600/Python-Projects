from random import randint

pass_length = int(input("Enter Password Length : "))

letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "!@#$%^&*()_-+=<>"

password = ""
for i in range(pass_length):
    decide = randint(1,4)
    if decide == 1:
        random_letter = randint(0,len(letters) - 1)
        password += letters[random_letter]
    elif decide == 2:
        random_letter = randint(0,len(numbers) - 1)
        password += numbers[random_letter]
    elif decide == 3:
        random_letter = randint(0,len(symbols) - 1)
        password += symbols[random_letter]
    elif decide == 4:
        random_letter = randint(0,len(letters) - 1)
        password += letters[random_letter].upper()

print(password)

