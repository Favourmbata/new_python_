import random

number = random.randint(0,100)
print("Guess a magic number between 0 and 100")

guess = -1
while guess!= number:
  guess = eval(input("enter your guess"))
  if guess == number:
      print("Yes the number is ",number)
  elif guess > number:
      print("The number is too low ",number)


