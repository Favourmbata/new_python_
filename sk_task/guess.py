import random

guessed_number = random.randint(1,10)
print(guessed_number)
guess = int(input("Enter your number:"))
while guessed_number != guess:
    guess = int(input("Enter your number:"))
