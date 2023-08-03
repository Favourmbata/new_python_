numbers = [10,20,30,40,50]
total = 0
for value in numbers:
    total = total + value
print(total)


square = []
for value in  numbers:
    square.append(value * value)
print(square)


largest_number = max(square)
smallest_number = min(square)
difference = largest_number - smallest_number
print(difference)