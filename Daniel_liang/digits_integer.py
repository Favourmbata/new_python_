import math

number = float(input("enter an integer between 0 and 1000 -> "))

number = 999

first_digit = math.floor(number / 100)
second_digit = math.floor((number % 100) / 10)
third_digit = math.floor((number % 100) % 10)

sumofdigit = first_digit+second_digit+third_digit

print(first_digit)
print(second_digit)
print(third_digit)
print(sumofdigit)
