import random

counter = 1

while counter <= 10:
    winning_number = random.randint(1, 10)
    user_number = int(input("Enter number: "))
    if winning_number == user_number:
        print("You have won")
        exit()
    counter += 1