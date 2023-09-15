import random
random = random.randint(1,10)
guess_number = int(input("Enter a guess number"))

while guess_number != random:
    guess_number = eval(input("enter you guess number"))
    if guess_number == random:
     print("correct! you won")